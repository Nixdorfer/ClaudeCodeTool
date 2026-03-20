import re

from rank_bm25 import BM25Okapi

from embedder import Embedder
from store import Store


def _tokenize(text: str) -> list[str]:
    text = re.sub(r"([a-z])([A-Z])", r"\1 \2", text)
    text = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1 \2", text)
    tokens = re.split(r"[\s_\-./\\:]+", text.lower())
    return [t for t in tokens if len(t) > 1]


class Searcher:
    def __init__(self, store: Store, embedder: Embedder, config: dict):
        self._store = store
        self._embedder = embedder
        self._dense_weight = config["dense_weight"]
        self._sparse_weight = config["sparse_weight"]

    def search(self, query: str, top_k: int, file_pattern: str = "") -> list[dict]:
        query_vec = self._embedder.embed_query(query)
        dense = self._store.search_vector(query_vec, top_k * 2, file_pattern)
        sparse = self._bm25_search(query, top_k * 2, file_pattern)
        fused = self._rrf_fuse(dense, sparse)
        return fused[:top_k]

    def _bm25_search(self, query: str, top_k: int, file_pattern: str = "") -> list[dict]:
        all_docs = self._store.get_all_contents(file_pattern)
        if not all_docs:
            return []
        corpus = [_tokenize(d["content"] + " " + d.get("symbol_name", "")) for d in all_docs]
        bm25 = BM25Okapi(corpus)
        q_tokens = _tokenize(query)
        scores = bm25.get_scores(q_tokens)
        indexed = sorted(enumerate(scores), key=lambda x: x[1], reverse=True)[:top_k]
        results = []
        for idx, score in indexed:
            if score > 0:
                doc = dict(all_docs[idx])
                doc["_score"] = float(score)
                results.append(doc)
        return results

    def _rrf_fuse(self, dense_results: list[dict], sparse_results: list[dict], k: int = 60) -> list[dict]:
        dense_ids = {r["id"]: i for i, r in enumerate(dense_results)}
        sparse_ids = {r["id"]: i for i, r in enumerate(sparse_results)}
        all_ids = set(dense_ids) | set(sparse_ids)
        scores: dict[str, float] = {}
        for rid in all_ids:
            d_rank = dense_ids.get(rid, len(dense_results))
            s_rank = sparse_ids.get(rid, len(sparse_results))
            scores[rid] = (
                self._dense_weight * (1.0 / (k + d_rank + 1))
                + self._sparse_weight * (1.0 / (k + s_rank + 1))
            )
        all_docs = {r["id"]: r for r in dense_results}
        all_docs.update({r["id"]: r for r in sparse_results})
        ranked = sorted(all_ids, key=lambda rid: scores[rid], reverse=True)
        result = []
        for rid in ranked:
            doc = dict(all_docs[rid])
            doc["score"] = scores[rid]
            result.append(doc)
        return result
