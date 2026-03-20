import numpy as np


class Embedder:
    def __init__(self, config: dict, device: str):
        self.model_name = config["model"]
        self.dimension = config["dimension"]
        self.batch_size = config["batch_size_gpu"] if device == "cuda" else config["batch_size_cpu"]
        self.max_length = config["max_length"]
        self.doc_prefix = config["doc_prefix"]
        self.query_prefix = config["query_prefix"]
        self.device = device
        self._model = None

    def _load(self):
        if self._model is None:
            from sentence_transformers import SentenceTransformer
            self._model = SentenceTransformer(self.model_name, device=self.device, trust_remote_code=True)

    def embed_documents(self, texts: list[str]) -> np.ndarray:
        self._load()
        prefixed = [self.doc_prefix + t for t in texts]
        return self._model.encode(
            prefixed,
            batch_size=self.batch_size,
            show_progress_bar=False,
            normalize_embeddings=True,
            convert_to_numpy=True,
        )

    def embed_query(self, query: str) -> np.ndarray:
        self._load()
        return self._model.encode(
            self.query_prefix + query,
            normalize_embeddings=True,
            convert_to_numpy=True,
        )
