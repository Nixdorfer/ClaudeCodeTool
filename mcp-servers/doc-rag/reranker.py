import asyncio


class BGEReranker:
    def __init__(self, config: dict, device: str):
        rer_cfg = config.get("models", {}).get("reranker", {})
        self.model_name: str = rer_cfg.get("name", "BAAI/bge-reranker-v2-m3")
        self.max_length: int = rer_cfg.get("max_length", 1024)
        self.device = device

        if device == "cuda":
            self.use_fp16: bool = rer_cfg.get("use_fp16", True)
            self.batch_size: int = rer_cfg.get("batch_size_gpu", 32)
        else:
            self.use_fp16 = False
            self.batch_size: int = rer_cfg.get("batch_size_cpu", 4)

        self._model = None

    async def load(self) -> None:
        loop = asyncio.get_event_loop()
        self._model = await loop.run_in_executor(None, self._load_sync)

    def _load_sync(self):
        from FlagEmbedding import FlagReranker
        return FlagReranker(
            self.model_name,
            use_fp16=self.use_fp16,
            device=self.device,
        )

    def _rerank_sync(self, pairs: list[list[str]]) -> list[float]:
        return self._model.compute_score(pairs, batch_size=self.batch_size, max_length=self.max_length)

    async def rerank(self, query: str, passages: list[str], top_k: int = 5) -> list[tuple[int, float]]:
        if not passages:
            return []
        pairs = [[query, p] for p in passages]
        loop = asyncio.get_event_loop()
        scores = await loop.run_in_executor(None, self._rerank_sync, pairs)
        if isinstance(scores, float):
            scores = [scores]
        indexed = sorted(enumerate(scores), key=lambda x: x[1], reverse=True)
        return [(idx, float(score)) for idx, score in indexed[:top_k]]
