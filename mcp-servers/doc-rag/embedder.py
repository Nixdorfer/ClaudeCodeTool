import asyncio
import struct
import numpy as np
from dataclasses import dataclass


@dataclass
class EmbeddingResult:
    dense: np.ndarray
    sparse: list[dict]
    colbert: list[np.ndarray] | None


class BGEM3Embedder:
    def __init__(self, config: dict, device: str):
        emb_cfg = config.get("models", {}).get("embedding", {})
        self.model_name: str = emb_cfg.get("name", "BAAI/bge-m3")
        self.max_length: int = emb_cfg.get("max_length", 8192)
        self.store_colbert: bool = emb_cfg.get("store_colbert", False)
        self.dimensions: int = emb_cfg.get("dimensions", 1024)
        self.device = device

        if device == "cuda":
            self.use_fp16: bool = emb_cfg.get("use_fp16", True)
            self.batch_size: int = emb_cfg.get("batch_size_gpu", 32)
        else:
            self.use_fp16 = False
            self.batch_size: int = emb_cfg.get("batch_size_cpu", 4)

        self._model = None

    async def load(self) -> None:
        loop = asyncio.get_event_loop()
        self._model = await loop.run_in_executor(None, self._load_sync)

    def _load_sync(self):
        from FlagEmbedding import BGEM3FlagModel
        return BGEM3FlagModel(
            self.model_name,
            use_fp16=self.use_fp16,
            device=self.device,
        )

    def _encode_sync(self, texts: list[str]) -> dict:
        return self._model.encode(
            texts,
            batch_size=self.batch_size,
            max_length=self.max_length,
            return_dense=True,
            return_sparse=True,
            return_colbert_vecs=self.store_colbert,
        )

    async def encode_chunks(self, texts: list[str]) -> EmbeddingResult:
        loop = asyncio.get_event_loop()
        output = await loop.run_in_executor(None, self._encode_sync, texts)
        dense = np.array(output["dense_vecs"], dtype=np.float32)
        sparse = output["lexical_weights"]
        colbert = output.get("colbert_vecs") if self.store_colbert else None
        return EmbeddingResult(dense=dense, sparse=sparse, colbert=colbert)

    async def encode_query(self, query: str) -> EmbeddingResult:
        result = await self.encode_chunks([query])
        dense = result.dense[0]
        sparse = result.sparse[0] if result.sparse else {}
        colbert = [result.colbert[0]] if result.colbert else None
        return EmbeddingResult(dense=dense, sparse=[sparse], colbert=colbert)

    def serialize_colbert(self, vec: np.ndarray) -> bytes:
        seq_len = vec.shape[0]
        header = struct.pack("<I", seq_len)
        return header + vec.astype(np.float32).tobytes()

    def deserialize_colbert(self, data: bytes) -> np.ndarray:
        seq_len = struct.unpack("<I", data[:4])[0]
        arr = np.frombuffer(data[4:], dtype=np.float32)
        dim = arr.size // seq_len
        return arr.reshape(seq_len, dim)
