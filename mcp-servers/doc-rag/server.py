import asyncio
import os
from pathlib import Path

import xxhash
import yaml
from mcp.server.fastmcp import FastMCP

from embedder import BGEM3Embedder
from reranker import BGEReranker
from parser import DocumentParser
from chunker import SemanticChunker
from store import LanceStore
from searcher import HybridSearcher

mcp = FastMCP("doc-rag")

_config: dict | None = None
_instances: dict[str, dict] = {}


def _load_config() -> dict:
    global _config
    if _config is None:
        cfg_path = Path(__file__).parent / "config.yaml"
        with open(cfg_path, "r", encoding="utf-8") as f:
            _config = yaml.safe_load(f)
    return _config


def _resolve_device(config: dict) -> str:
    device = config.get("device", "auto")
    if device != "auto":
        return device
    try:
        import torch
        if torch.cuda.is_available():
            return "cuda"
        if torch.backends.mps.is_available():
            return "mps"
    except ImportError:
        pass
    return "cpu"


def _get_index_dir(project_dir: str) -> str:
    config = _load_config()
    index_rel = config.get("store", {}).get("index_dir", ".claude/doc-rag")
    if project_dir:
        return str(Path(project_dir) / index_rel)
    return str(Path.home() / index_rel)


def _compute_hash(file_path: str) -> str:
    h = xxhash.xxh128()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


async def _ensure_init(project_dir: str) -> dict:
    key = project_dir or "__default__"
    if key in _instances:
        return _instances[key]

    config = _load_config()
    device = _resolve_device(config)
    index_dir = _get_index_dir(project_dir)

    embedder = BGEM3Embedder(config, device)
    await embedder.load()

    reranker = BGEReranker(config, device)
    await reranker.load()

    dims = config.get("models", {}).get("embedding", {}).get("dimensions", 1024)
    store = LanceStore(index_dir, dims)
    searcher = HybridSearcher(store, embedder, reranker, config)
    parser = DocumentParser(config, device)
    chunker = SemanticChunker(config)

    _instances[key] = {
        "config": config,
        "embedder": embedder,
        "reranker": reranker,
        "store": store,
        "searcher": searcher,
        "parser": parser,
        "chunker": chunker,
    }
    return _instances[key]


def _collect_files(path: str, supported: list[str], file_filter: str) -> list[str]:
    p = Path(path)
    if p.is_file():
        return [str(p)] if p.suffix.lower() in supported else []
    files = []
    for ext in supported:
        files.extend(p.rglob(f"*{ext}"))
    result = [str(f) for f in files]
    if file_filter:
        result = [f for f in result if file_filter.lower() in f.lower()]
    return result


@mcp.tool()
async def index_documents(path: str, project_dir: str = "", force: bool = False, file_filter: str = "") -> dict:
    try:
        ctx = await _ensure_init(project_dir)
        config = ctx["config"]
        supported = config.get("supported_formats", [".pdf", ".md", ".txt"])
        files = _collect_files(path, supported, file_filter)

        indexed = 0
        skipped = 0
        failed = 0
        errors = []
        total_chunks = 0

        for file_path in files:
            try:
                content_hash = _compute_hash(file_path)
                store: LanceStore = ctx["store"]
                if not force and store.has_document(file_path, content_hash):
                    skipped += 1
                    continue
                elements = await ctx["parser"].parse(file_path)
                chunks = ctx["chunker"].chunk(elements, file_path)
                if not chunks:
                    skipped += 1
                    continue
                texts = [c.text for c in chunks]
                embeddings = await ctx["embedder"].encode_chunks(texts)
                store.remove_by_source(file_path)
                store.upsert(chunks, embeddings, content_hash)
                indexed += 1
                total_chunks += len(chunks)
            except Exception as e:
                failed += 1
                errors.append(f"{file_path}: {e}")

        return {"indexed": indexed, "skipped": skipped, "failed": failed, "errors": errors, "total_chunks": total_chunks}
    except Exception as e:
        return {"indexed": 0, "skipped": 0, "failed": 0, "errors": [str(e)], "total_chunks": 0}


@mcp.tool()
async def search_docs(query: str, project_dir: str = "", top_k: int = 0, source_filter: str = "") -> dict:
    try:
        ctx = await _ensure_init(project_dir)
        results = await ctx["searcher"].search(query, top_k, source_filter)
        return {
            "results": [r.to_dict() for r in results],
            "total_indexed": ctx["store"].count_chunks(),
        }
    except Exception as e:
        return {"results": [], "total_indexed": 0, "error": str(e)}


@mcp.tool()
async def get_doc_summary(project_dir: str = "") -> dict:
    try:
        ctx = await _ensure_init(project_dir)
        return ctx["store"].summary()
    except Exception as e:
        return {"total_documents": 0, "total_chunks": 0, "index_size_mb": 0, "documents": [], "error": str(e)}


@mcp.tool()
async def remove_documents(paths: str, project_dir: str = "") -> dict:
    try:
        ctx = await _ensure_init(project_dir)
        store: LanceStore = ctx["store"]
        path_list = [p.strip() for p in paths.split(",") if p.strip()]
        removed = 0
        not_found = []
        for p in path_list:
            count = store.remove_by_source(p)
            if count > 0:
                removed += count
            else:
                not_found.append(p)
        return {"removed": removed, "not_found": not_found}
    except Exception as e:
        return {"removed": 0, "not_found": [], "error": str(e)}


@mcp.tool()
async def list_indexed_docs(project_dir: str = "") -> dict:
    try:
        ctx = await _ensure_init(project_dir)
        return {"documents": ctx["store"].list_documents()}
    except Exception as e:
        return {"documents": [], "error": str(e)}


if __name__ == "__main__":
    mcp.run(transport="stdio")
