import re
from dataclasses import dataclass, field

from parser import DocElement, ElementType


@dataclass
class Chunk:
    text: str
    source: str
    chunk_type: str
    page: int | None = None
    chunk_index: int = 0
    metadata: dict = field(default_factory=dict)


class SemanticChunker:
    def __init__(self, config: dict):
        cfg = config.get("chunker", {})
        self.max_chunk_size: int = cfg.get("max_chunk_size", 512)
        self.min_chunk_size: int = cfg.get("min_chunk_size", 64)
        self.overlap: int = cfg.get("overlap", 64)
        self.table_as_single_chunk: bool = cfg.get("table_as_single_chunk", True)
        self.use_jieba: bool = cfg.get("use_jieba", True)
        if self.use_jieba:
            import jieba
            self._jieba = jieba

    def chunk(self, elements: list[DocElement], source: str) -> list[Chunk]:
        chunks: list[Chunk] = []
        pending_title: str = ""
        idx = 0

        for el in elements:
            if el.type == ElementType.TITLE:
                pending_title = el.text
                continue

            if el.type == ElementType.TABLE and self.table_as_single_chunk:
                text = f"{pending_title}\n{el.text}".strip() if pending_title else el.text
                chunks.append(Chunk(text=text, source=source, chunk_type="table", page=el.page, chunk_index=idx))
                idx += 1
                pending_title = ""
                continue

            parts = self._split_text(el.text)
            for i, part in enumerate(parts):
                if pending_title:
                    part = f"{pending_title}\n{part}"
                    pending_title = ""
                is_last = i == len(parts) - 1
                if self._estimate_tokens(part) >= self.min_chunk_size or (is_last and not chunks):
                    chunks.append(Chunk(text=part, source=source, chunk_type="text", page=el.page, chunk_index=idx))
                    idx += 1

        return chunks

    def _split_text(self, text: str) -> list[str]:
        sentences = self._split_sentences(text)
        if not sentences:
            return []
        results: list[str] = []
        current: list[str] = []
        current_tokens = 0

        for sent in sentences:
            sent_tokens = self._estimate_tokens(sent)
            if current_tokens + sent_tokens > self.max_chunk_size and current:
                results.append(" ".join(current))
                overlap_sents = self._get_overlap_sentences(current)
                current = overlap_sents
                current_tokens = sum(self._estimate_tokens(s) for s in current)
            current.append(sent)
            current_tokens += sent_tokens

        if current:
            results.append(" ".join(current))
        return results if results else [text.strip()]

    def _get_overlap_sentences(self, sentences: list[str]) -> list[str]:
        result: list[str] = []
        total = 0
        for sent in reversed(sentences):
            t = self._estimate_tokens(sent)
            if total + t > self.overlap:
                break
            result.insert(0, sent)
            total += t
        return result

    def _split_sentences(self, text: str) -> list[str]:
        parts = re.split(r"(?<=[。！？.!?\n])", text)
        return [p.strip() for p in parts if p.strip()]

    def _estimate_tokens(self, text: str) -> int:
        chinese = len(re.findall(r"[\u4e00-\u9fff]", text))
        if chinese > len(text) * 0.3:
            if self.use_jieba:
                words = list(self._jieba.cut(text))
                return int(len(words) * 1.2)
            return int(chinese * 1.5)
        return max(int(len(text.split()) * 1.3), len(text) // 4)

    def tokenize_for_sparse(self, text: str) -> list[str]:
        chinese = len(re.findall(r"[\u4e00-\u9fff]", text))
        if chinese > len(text) * 0.3 and self.use_jieba:
            return list(self._jieba.cut_for_search(text))
        return text.lower().split()
