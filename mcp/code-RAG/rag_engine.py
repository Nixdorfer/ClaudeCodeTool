import lancedb
import pyarrow as pa
from sentence_transformers import SentenceTransformer
from pathlib import Path
from typing import Optional
import hashlib
import json
import logging
import os
import time
import uuid

logger = logging.getLogger(__name__)

SUPPORTED_EXTENSIONS = {
    ".rs", ".ts", ".tsx", ".js", ".jsx", ".vue", ".py",
    ".toml", ".json", ".yaml", ".yml", ".md",
    ".glsl", ".wgsl", ".html", ".css", ".scss",
}

IGNORE_DIRS = {
    "node_modules", ".git", "target", "dist", "build",
    "__pycache__", ".cache", "pkg", "wasm-pack-out",
    ".claude", "venv", ".venv", "env", ".env",
    "runtime", ".idea", ".vscode", ".next",
    "coverage", ".nyc_output", ".turbo",
}

IGNORE_FILES = {
    "pnpm-lock.yaml", "package-lock.json", "yarn.lock",
    "Cargo.lock", "poetry.lock", "composer.lock",
}

MAX_FILE_SIZE = 256 * 1024
BATCH_SIZE = 64

CODE_SCHEMA = pa.schema([
    pa.field("id", pa.utf8()),
    pa.field("content", pa.utf8()),
    pa.field("source", pa.utf8()),
    pa.field("start_line", pa.int32()),
    pa.field("end_line", pa.int32()),
    pa.field("language", pa.utf8()),
    pa.field("vector", pa.list_(pa.float32(), 384)),
])

KNOWLEDGE_SCHEMA = pa.schema([
    pa.field("id", pa.utf8()),
    pa.field("title", pa.utf8()),
    pa.field("content", pa.utf8()),
    pa.field("category", pa.utf8()),
    pa.field("tags", pa.utf8()),
    pa.field("timestamp", pa.float64()),
    pa.field("vector", pa.list_(pa.float32(), 384)),
])


def _ext_to_lang(ext: str) -> str:
    mapping = {
        ".rs": "rust", ".ts": "typescript", ".tsx": "typescript",
        ".js": "javascript", ".jsx": "javascript", ".vue": "vue",
        ".py": "python", ".toml": "toml", ".json": "json",
        ".yaml": "yaml", ".yml": "yaml", ".md": "markdown",
        ".glsl": "glsl", ".wgsl": "wgsl", ".html": "html",
        ".css": "css", ".scss": "scss",
    }
    return mapping.get(ext, "text")


def _chunk_by_lines(text: str, chunk_lines: int = 60, overlap_lines: int = 10) -> list[tuple[int, int, str]]:
    lines = text.split("\n")
    if len(lines) <= chunk_lines:
        return [(1, len(lines), text)]
    chunks = []
    step = chunk_lines - overlap_lines
    for i in range(0, len(lines), step):
        end = min(i + chunk_lines, len(lines))
        chunk = "\n".join(lines[i:end])
        chunks.append((i + 1, end, chunk))
        if end >= len(lines):
            break
    return chunks


def _file_hash(content: str) -> str:
    return hashlib.sha256(content.encode("utf-8")).hexdigest()[:16]


class RAGEngine:
    def __init__(self, db_path: str, model_name: str = "all-MiniLM-L6-v2"):
        self.db_path = db_path
        self.db = lancedb.connect(db_path)
        self.model = SentenceTransformer(model_name)
        self.table: Optional[lancedb.table.Table] = None
        self.knowledge_table: Optional[lancedb.table.Table] = None
        self.hash_cache_path = os.path.join(db_path, "file_hashes.json")
        self._file_hashes: dict[str, str] = {}
        self._load_hashes()
        self._try_open_table()
        self._try_open_knowledge_table()
        self._validate_cache()

    def _load_hashes(self):
        if os.path.exists(self.hash_cache_path):
            try:
                with open(self.hash_cache_path, "r") as f:
                    self._file_hashes = json.load(f)
            except Exception:
                self._file_hashes = {}

    def _save_hashes(self):
        os.makedirs(os.path.dirname(self.hash_cache_path), exist_ok=True)
        with open(self.hash_cache_path, "w") as f:
            json.dump(self._file_hashes, f)

    def _try_open_table(self):
        try:
            self.table = self.db.open_table("code_chunks")
        except Exception:
            self.table = None

    def _validate_cache(self):
        if self._file_hashes and self.table is None:
            logger.info("Hash cache exists but code_chunks table missing — clearing cache for full re-index")
            self._file_hashes = {}
            self._save_hashes()
        elif self.table is not None and self._file_hashes:
            try:
                table_count = self.table.count_rows()
                if table_count == 0:
                    logger.info("code_chunks table empty but cache non-empty — clearing cache")
                    self._file_hashes = {}
                    self._save_hashes()
            except Exception:
                pass

    def _collect_files(self, directory: str) -> list[Path]:
        root = Path(directory)
        files = []
        for dirpath, dirnames, filenames in os.walk(root):
            dirnames[:] = [d for d in dirnames if d not in IGNORE_DIRS]
            for fname in filenames:
                if fname in IGNORE_FILES:
                    continue
                fpath = Path(dirpath) / fname
                if fpath.suffix not in SUPPORTED_EXTENSIONS:
                    continue
                try:
                    if fpath.stat().st_size > MAX_FILE_SIZE:
                        continue
                except OSError:
                    continue
                files.append(fpath)
        return files

    def _batch_encode(self, texts: list[str]) -> list[list[float]]:
        results = []
        for i in range(0, len(texts), BATCH_SIZE):
            batch = texts[i:i + BATCH_SIZE]
            embeddings = self.model.encode(batch, show_progress_bar=False)
            results.extend(embeddings.tolist())
        return results

    def index_directory(self, directory: str) -> dict:
        files = self._collect_files(directory)
        logger.info(f"Collected {len(files)} source files")

        pending_chunks: list[dict] = []
        pending_texts: list[str] = []
        indexed_files = 0
        skipped_files = 0

        for file_path in files:
            try:
                content = file_path.read_text(encoding="utf-8", errors="ignore")
            except Exception:
                continue

            file_key = str(file_path)
            content_hash = _file_hash(content)

            if self._file_hashes.get(file_key) == content_hash:
                skipped_files += 1
                continue

            lang = _ext_to_lang(file_path.suffix)
            chunks = _chunk_by_lines(content)

            for start, end, chunk_text in chunks:
                if len(chunk_text.strip()) < 10:
                    continue
                chunk_id = f"{file_key}:{start}-{end}"
                pending_chunks.append({
                    "id": chunk_id,
                    "content": chunk_text,
                    "source": file_key,
                    "start_line": start,
                    "end_line": end,
                    "language": lang,
                })
                pending_texts.append(chunk_text)

            self._file_hashes[file_key] = content_hash
            indexed_files += 1

        if pending_texts:
            logger.info(f"Encoding {len(pending_texts)} chunks...")
            vectors = self._batch_encode(pending_texts)
            for chunk, vec in zip(pending_chunks, vectors):
                chunk["vector"] = vec

        if pending_chunks:
            if self.table is not None:
                stale_sources = {c["source"] for c in pending_chunks}
                try:
                    existing = self.table.to_arrow()
                    source_col = existing.column("source").to_pylist()
                    keep_mask = [s not in stale_sources for s in source_col]
                    keep_table = existing.filter(keep_mask)
                    merged = keep_table.to_pylist()
                    merged.extend(pending_chunks)
                    self.table = self.db.create_table("code_chunks", data=merged, schema=CODE_SCHEMA, mode="overwrite")
                except Exception:
                    self.table = self.db.create_table("code_chunks", data=pending_chunks, schema=CODE_SCHEMA, mode="overwrite")
            else:
                self.table = self.db.create_table("code_chunks", data=pending_chunks, schema=CODE_SCHEMA, mode="overwrite")

        self._save_hashes()

        return {
            "total_files": len(files),
            "indexed": indexed_files,
            "skipped_unchanged": skipped_files,
            "chunks_created": len(pending_chunks),
        }

    def search(self, query: str, top_k: int = 10, language: Optional[str] = None) -> list[dict]:
        if self.table is None:
            return []

        query_vec = self.model.encode(query).tolist()
        builder = self.table.search(query_vec).limit(top_k)

        if language:
            builder = builder.where(f"language = '{language}'")

        try:
            results = builder.to_list()
        except Exception as e:
            logger.error(f"Search failed: {e}")
            return []

        return [
            {
                "content": r["content"],
                "source": r["source"],
                "start_line": r["start_line"],
                "end_line": r["end_line"],
                "language": r["language"],
                "score": float(1.0 / (1.0 + r.get("_distance", 0))),
            }
            for r in results
        ]

    def get_status(self) -> dict:
        self._try_open_table()
        if self.table is None:
            return {"indexed": False, "total_chunks": 0, "total_files": 0}
        try:
            count = self.table.count_rows()
            arrow_table = self.table.to_arrow()
            sources = len(set(arrow_table.column("source").to_pylist()))
        except Exception:
            count = 0
            sources = 0
        return {"indexed": True, "total_chunks": count, "total_files": sources}

    def clear(self):
        try:
            self.db.drop_table("code_chunks")
        except Exception:
            pass
        self.table = None
        self._file_hashes = {}
        self._save_hashes()

    def _try_open_knowledge_table(self):
        try:
            self.knowledge_table = self.db.open_table("knowledge")
        except Exception:
            self.knowledge_table = None

    def add_knowledge(self, title: str, content: str, category: str = "general", tags: list[str] | None = None) -> dict:
        entry_id = uuid.uuid4().hex[:12]
        tags_str = ",".join(tags) if tags else ""
        embed_text = f"{title}\n{content}"
        vector = self.model.encode(embed_text).tolist()

        record = {
            "id": entry_id,
            "title": title,
            "content": content,
            "category": category,
            "tags": tags_str,
            "timestamp": time.time(),
            "vector": vector,
        }

        if self.knowledge_table is not None:
            self.knowledge_table.add([record])
        else:
            self.knowledge_table = self.db.create_table("knowledge", data=[record], schema=KNOWLEDGE_SCHEMA, mode="overwrite")

        return {"id": entry_id, "title": title, "category": category}

    def search_knowledge(self, query: str, top_k: int = 10, category: str | None = None) -> list[dict]:
        if self.knowledge_table is None:
            return []

        query_vec = self.model.encode(query).tolist()
        builder = self.knowledge_table.search(query_vec).limit(top_k)

        if category:
            builder = builder.where(f"category = '{category}'")

        try:
            results = builder.to_list()
        except Exception as e:
            logger.error(f"Knowledge search failed: {e}")
            return []

        return [
            {
                "id": r["id"],
                "title": r["title"],
                "content": r["content"],
                "category": r["category"],
                "tags": r["tags"].split(",") if r["tags"] else [],
                "score": float(1.0 / (1.0 + r.get("_distance", 0))),
            }
            for r in results
        ]

    def remove_knowledge(self, entry_id: str) -> bool:
        if self.knowledge_table is None:
            return False
        try:
            self.knowledge_table.delete(f"id = '{entry_id}'")
            return True
        except Exception as e:
            logger.error(f"Knowledge remove failed: {e}")
            return False

    def list_knowledge(self, category: str | None = None) -> list[dict]:
        if self.knowledge_table is None:
            return []
        try:
            rows = self.knowledge_table.to_arrow().to_pylist()
            if category:
                rows = [r for r in rows if r["category"] == category]
            rows.sort(key=lambda r: r.get("timestamp", 0), reverse=True)
            return [
                {
                    "id": r["id"],
                    "title": r["title"],
                    "category": r["category"],
                    "tags": r["tags"].split(",") if r["tags"] else [],
                }
                for r in rows
            ]
        except Exception:
            return []

    def get_knowledge_status(self) -> dict:
        if self.knowledge_table is None:
            return {"has_knowledge": False, "total_entries": 0, "categories": []}
        try:
            rows = self.knowledge_table.to_arrow().to_pylist()
            categories = list({r["category"] for r in rows})
            return {
                "has_knowledge": True,
                "total_entries": len(rows),
                "categories": categories,
            }
        except Exception:
            return {"has_knowledge": False, "total_entries": 0, "categories": []}
