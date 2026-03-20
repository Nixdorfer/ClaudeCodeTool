import json
from datetime import datetime, timezone
from pathlib import Path

import lancedb
import numpy as np
import pyarrow as pa

from embedder import EmbeddingResult
from chunker import Chunk


SCHEMA = pa.schema([
    pa.field("dense_vector", pa.list_(pa.float32(), 1024)),
    pa.field("sparse_json", pa.string()),
    pa.field("colbert_bytes", pa.binary()),
    pa.field("text", pa.string()),
    pa.field("source", pa.string()),
    pa.field("chunk_type", pa.string()),
    pa.field("page", pa.int32()),
    pa.field("chunk_index", pa.int32()),
    pa.field("content_hash", pa.string()),
    pa.field("indexed_at", pa.string()),
])

TABLE_NAME = "doc_chunks"


class LanceStore:
    def __init__(self, index_dir: str, dimensions: int = 1024):
        self.index_dir = index_dir
        self.dimensions = dimensions
        Path(index_dir).mkdir(parents=True, exist_ok=True)
        self._db = lancedb.connect(index_dir)
        self._table = None

    def _ensure_table(self):
        if self._table is not None:
            return
        existing = self._db.table_names()
        if TABLE_NAME in existing:
            self._table = self._db.open_table(TABLE_NAME)
        else:
            self._table = None

    def upsert(self, chunks: list[Chunk], embeddings: EmbeddingResult, content_hash: str) -> None:
        now = datetime.now(timezone.utc).isoformat()
        rows = []
        for i, chunk in enumerate(chunks):
            sparse = embeddings.sparse[i] if i < len(embeddings.sparse) else {}
            colbert_bytes = b""
            if embeddings.colbert and i < len(embeddings.colbert):
                vec = np.array(embeddings.colbert[i], dtype=np.float32)
                colbert_bytes = vec.tobytes()
            rows.append({
                "dense_vector": embeddings.dense[i].tolist(),
                "sparse_json": json.dumps({str(k): float(v) for k, v in sparse.items()}),
                "colbert_bytes": colbert_bytes,
                "text": chunk.text,
                "source": chunk.source,
                "chunk_type": chunk.chunk_type,
                "page": chunk.page if chunk.page is not None else -1,
                "chunk_index": chunk.chunk_index,
                "content_hash": content_hash,
                "indexed_at": now,
            })
        if not rows:
            return
        self._ensure_table()
        if self._table is None:
            self._table = self._db.create_table(TABLE_NAME, data=rows, schema=SCHEMA)
        else:
            self._table.add(rows)

    def has_document(self, source: str, content_hash: str) -> bool:
        self._ensure_table()
        if self._table is None:
            return False
        results = self._table.search().where(f"source = '{source}' AND content_hash = '{content_hash}'").limit(1).to_list()
        return len(results) > 0

    def remove_by_source(self, source: str) -> int:
        self._ensure_table()
        if self._table is None:
            return 0
        before = self._table.count_rows()
        self._table.delete(f"source = '{source}'")
        after = self._table.count_rows()
        return before - after

    def dense_search(self, query_vector: np.ndarray, top_k: int, source_filter: str = "") -> list[dict]:
        self._ensure_table()
        if self._table is None:
            return []
        q = self._table.search(query_vector.tolist(), vector_column_name="dense_vector").limit(top_k)
        if source_filter:
            q = q.where(f"source LIKE '%{source_filter}%'")
        return q.to_list()

    def full_scan(self, source_filter: str = "") -> list[dict]:
        self._ensure_table()
        if self._table is None:
            return []
        q = self._table.search()
        if source_filter:
            q = q.where(f"source LIKE '%{source_filter}%'")
        rows = q.to_list()
        return [
            {
                "text": r["text"],
                "source": r["source"],
                "chunk_type": r["chunk_type"],
                "page": r["page"],
                "chunk_index": r["chunk_index"],
                "sparse_json": r["sparse_json"],
            }
            for r in rows
        ]

    def count_documents(self) -> int:
        self._ensure_table()
        if self._table is None:
            return 0
        rows = self._table.search().select(["source"]).to_list()
        return len({r["source"] for r in rows})

    def count_chunks(self) -> int:
        self._ensure_table()
        if self._table is None:
            return 0
        return self._table.count_rows()

    def summary(self) -> dict:
        self._ensure_table()
        docs = self.list_documents()
        size_mb = sum(
            f.stat().st_size for f in Path(self.index_dir).rglob("*") if f.is_file()
        ) / (1024 * 1024)
        return {
            "total_documents": len(docs),
            "total_chunks": self.count_chunks(),
            "index_size_mb": round(size_mb, 2),
            "documents": docs,
        }

    def list_documents(self) -> list[dict]:
        self._ensure_table()
        if self._table is None:
            return []
        rows = self._table.search().select(["source", "chunk_index", "indexed_at"]).to_list()
        groups: dict[str, dict] = {}
        for r in rows:
            src = r["source"]
            if src not in groups:
                groups[src] = {"source": src, "chunks": 0, "last_indexed": r["indexed_at"]}
            groups[src]["chunks"] += 1
            if r["indexed_at"] > groups[src]["last_indexed"]:
                groups[src]["last_indexed"] = r["indexed_at"]
        return list(groups.values())
