import sys
import os
import time
import hashlib
from pathlib import Path

import yaml
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("code-rag")

_config: dict | None = None
_instances: dict[str, object] = {}


def _load_config() -> dict:
    global _config
    if _config is None:
        cfg_path = Path(__file__).parent / "config.yaml"
        _config = yaml.safe_load(cfg_path.read_text(encoding="utf-8"))
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


def _get_data_dir(project_path: str) -> Path:
    return Path(project_path) / ".claude" / "code-rag"


def _ensure_init(project_path: str):
    if project_path in _instances:
        return
    cfg = _load_config()
    device = _resolve_device(cfg)
    sys.path.insert(0, str(Path(__file__).parent))
    from embedder import Embedder
    from store import Store
    from searcher import Searcher
    data_dir = _get_data_dir(project_path)
    embedder = Embedder(cfg["embedding"], device)
    store = Store(data_dir)
    searcher = Searcher(store, embedder, cfg["search"])
    _instances[project_path] = {"embedder": embedder, "store": store, "searcher": searcher, "device": device, "config": cfg}


def _collect_files(root: Path, index_config: dict) -> list[Path]:
    import fnmatch
    extensions = set(index_config["file_extensions"])
    ignore_patterns = index_config.get("ignore_patterns", [])
    files = []
    for f in root.rglob("*"):
        if not f.is_file():
            continue
        if f.suffix.lower() not in extensions:
            continue
        rel = f.relative_to(root).as_posix()
        if any(fnmatch.fnmatch(rel, pat) for pat in ignore_patterns):
            continue
        files.append(f)
    return files


def _file_hash(path: Path) -> str:
    return hashlib.md5(path.read_bytes()).hexdigest()


@mcp.tool()
def index_codebase(project_path: str, force: bool = False) -> dict:
    try:
        _ensure_init(project_path)
        ctx = _instances[project_path]
        store = ctx["store"]
        embedder = ctx["embedder"]
        cfg = ctx["config"]
        sys.path.insert(0, str(Path(__file__).parent))
        from parser import CodeParser
        from chunker import Chunker
        t0 = time.time()
        root = Path(project_path)
        files = _collect_files(root, cfg["index"])
        parser = CodeParser()
        chunker = Chunker(cfg["chunking"])
        files_indexed = 0
        files_skipped = 0
        total_chunks = 0
        indexed_paths = set()
        for fpath in files:
            rel = fpath.as_posix()
            content_hash = _file_hash(fpath)
            indexed_paths.add(rel)
            if not force and not store.file_needs_index(rel, content_hash):
                files_skipped += 1
                continue
            try:
                source_text = fpath.read_text(encoding="utf-8", errors="replace")
                source_lines = source_text.splitlines()
                symbols = parser.parse_file(fpath)
                chunks = chunker.chunk_file(rel, symbols, source_lines)
                if not chunks:
                    files_skipped += 1
                    continue
                texts = [c.content for c in chunks]
                vecs = embedder.embed_documents(texts)
                records = [
                    {
                        "id": c.id, "file_path": c.file_path,
                        "start_line": c.start_line, "end_line": c.end_line,
                        "content": c.content, "symbol_name": c.symbol_name,
                        "symbol_type": c.symbol_type, "language": c.language,
                        "signature": c.signature, "context": c.context,
                        "vector": vecs[i].tolist(),
                    }
                    for i, c in enumerate(chunks)
                ]
                store.delete_by_file(rel)
                store.upsert_chunks(records)
                store.mark_indexed(rel, content_hash)
                files_indexed += 1
                total_chunks += len(chunks)
            except Exception as e:
                files_skipped += 1
        previously_indexed = store.get_indexed_files()
        deleted = previously_indexed - indexed_paths
        files_deleted = 0
        for dp in deleted:
            store.delete_by_file(dp)
            files_deleted += 1
        for dp in deleted:
            store._hashes.pop(dp, None)
        store.save_hashes()
        return {
            "status": "ok",
            "files_total": len(files),
            "files_indexed": files_indexed,
            "files_skipped": files_skipped,
            "files_deleted": files_deleted,
            "chunks_total": total_chunks,
            "duration_sec": round(time.time() - t0, 2),
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}


@mcp.tool()
def search_code(project_path: str, query: str, top_k: int = 10, file_pattern: str = "") -> list[dict]:
    try:
        _ensure_init(project_path)
        searcher = _instances[project_path]["searcher"]
        results = searcher.search(query, top_k, file_pattern)
        return [
            {
                "file": r.get("file_path", ""),
                "start_line": r.get("start_line", 0),
                "end_line": r.get("end_line", 0),
                "symbol_name": r.get("symbol_name", ""),
                "symbol_type": r.get("symbol_type", ""),
                "content": r.get("content", ""),
                "score": r.get("score", 0.0),
            }
            for r in results
        ]
    except Exception as e:
        return [{"error": str(e)}]


@mcp.tool()
def get_symbol_definition(project_path: str, symbol_name: str, symbol_type: str = "") -> list[dict]:
    try:
        _ensure_init(project_path)
        store = _instances[project_path]["store"]
        results = store.find_symbol(symbol_name, symbol_type)
        return [
            {
                "file": r.get("file_path", ""),
                "start_line": r.get("start_line", 0),
                "end_line": r.get("end_line", 0),
                "symbol_type": r.get("symbol_type", ""),
                "signature": r.get("signature", ""),
                "content": r.get("content", ""),
            }
            for r in results
        ]
    except Exception as e:
        return [{"error": str(e)}]


@mcp.tool()
def get_file_summary(project_path: str, file_path: str) -> dict:
    try:
        _ensure_init(project_path)
        store = _instances[project_path]["store"]
        symbols = store.get_file_symbols(file_path)
        sys.path.insert(0, str(Path(__file__).parent))
        from parser import LANG_MAP
        lang = LANG_MAP.get(Path(file_path).suffix.lower(), "")
        return {
            "file": file_path,
            "language": lang,
            "symbols": [
                {
                    "name": s.get("symbol_name", ""),
                    "type": s.get("symbol_type", ""),
                    "start_line": s.get("start_line", 0),
                    "end_line": s.get("end_line", 0),
                    "signature": s.get("signature", ""),
                }
                for s in symbols
            ],
        }
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def index_status(project_path: str) -> dict:
    try:
        _ensure_init(project_path)
        ctx = _instances[project_path]
        stats = ctx["store"].get_stats()
        stats["device"] = ctx["device"]
        return stats
    except Exception as e:
        return {"error": str(e)}


if __name__ == "__main__":
    mcp.run(transport="stdio")
