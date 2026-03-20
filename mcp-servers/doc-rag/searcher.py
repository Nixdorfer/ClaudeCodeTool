import json
from dataclasses import dataclass

import numpy as np

from store import LanceStore
from embedder import BGEM3Embedder
from reranker import BGEReranker


@dataclass
class SearchResult:
    text: str
    source: str
    page: int | None
    chunk_type: str
    score: float
    rerank_score: float
    chunk_index: int = 0

    def to_dict(self) -> dict:
        return {
            "text": self.text,
            "source": self.source,
            "page": self.page,
            "chunk_type": self.chunk_type,
            "score": self.score,
            "rerank_score": self.rerank_score,
            "chunk_index": self.chunk_index,
        }


class HybridSearcher:
    def __init__(self, store: LanceStore, embedder: BGEM3Embedder, reranker: BGEReranker, config: dict):
        self.store = store
        self.embedder = embedder
        self.reranker = reranker
        cfg = config.get("search", {})
        self.top_k: int = cfg.get("top_k", 20)
        self.rerank_top_k: int = cfg.get("rerank_top_k", 5)
        self.dense_weight: float = cfg.get("dense_weight", 0.6)
        self.sparse_weight: float = cfg.get("sparse_weight", 0.4)
        self.rrf_k: int = cfg.get("rrf_k", 60)

    async def search(self, query: str, top_k: int = 0, source_filter: str = "") -> list[SearchResult]:
        k = top_k or self.top_k
        query_emb = await self.embedder.encode_query(query)
        dense_results = self.store.dense_search(query_emb.dense, k, source_filter)
        sparse_q = query_emb.sparse[0] if query_emb.sparse else {}
        sparse_results = self._sparse_search(sparse_q, k, source_filter)
        fused = self._rrf_fusion(dense_results, sparse_results)
        top_fused = fused[:self.rerank_top_k]
        passages = [r["text"] for r in top_fused]
        reranked = await self.reranker.rerank(query, passages, self.rerank_top_k)
        results = []
        for orig_idx, rscore in reranked:
            row = top_fused[orig_idx]
            page = row.get("page")
            if page == -1:
                page = None
            results.append(SearchResult(
                text=row["text"],
                source=row["source"],
                page=page,
                chunk_type=row.get("chunk_type", "text"),
                score=row.get("_rrf_score", 0.0),
                rerank_score=rscore,
                chunk_index=row.get("chunk_index", 0),
            ))
        return results

    def _sparse_search(self, query_sparse: dict, top_k: int, source_filter: str) -> list[dict]:
        rows = self.store.full_scan(source_filter)
        scores: list[tuple[float, dict]] = []
        for row in rows:
            try:
                doc_sparse = json.loads(row.get("sparse_json", "{}"))
            except Exception:
                doc_sparse = {}
            score = sum(float(query_sparse.get(k, 0)) * float(v) for k, v in doc_sparse.items())
            scores.append((score, row))
        scores.sort(key=lambda x: x[0], reverse=True)
        return [r for _, r in scores[:top_k]]

    def _rrf_fusion(self, dense_results: list[dict], sparse_results: list[dict]) -> list[dict]:
        scores: dict[tuple, float] = {}
        rows_map: dict[tuple, dict] = {}

        for rank, row in enumerate(dense_results):
            key = (row["source"], row.get("chunk_index", 0))
            scores[key] = scores.get(key, 0.0) + self.dense_weight / (self.rrf_k + rank + 1)
            rows_map[key] = row

        for rank, row in enumerate(sparse_results):
            key = (row["source"], row.get("chunk_index", 0))
            scores[key] = scores.get(key, 0.0) + self.sparse_weight / (self.rrf_k + rank + 1)
            if key not in rows_map:
                rows_map[key] = row

        sorted_keys = sorted(scores.keys(), key=lambda k: scores[k], reverse=True)
        fused = []
        for key in sorted_keys:
            row = dict(rows_map[key])
            row["_rrf_score"] = scores[key]
            fused.append(row)
        return fused
