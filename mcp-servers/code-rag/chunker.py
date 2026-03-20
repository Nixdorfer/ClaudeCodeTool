from dataclasses import dataclass
from pathlib import Path

import xxhash

from parser import Symbol


@dataclass
class Chunk:
    id: str
    file_path: str
    start_line: int
    end_line: int
    content: str
    symbol_name: str
    symbol_type: str
    language: str
    signature: str
    context: str


IMPORT_KEYWORDS = {"import", "require", "use", "include", "from", "package", "namespace", "mod"}


def _make_id(file_path: str, start_line: int, end_line: int) -> str:
    return xxhash.xxh64(f"{file_path}:{start_line}:{end_line}").hexdigest()


def _lines_to_content(source_lines: list[str], start: int, end: int) -> str:
    return "\n".join(source_lines[start - 1:end])


class Chunker:
    def __init__(self, config: dict):
        self._max_lines = config["max_chunk_lines"]
        self._min_lines = config["min_chunk_lines"]

    def chunk_file(self, file_path: str, symbols: list[Symbol], source_lines: list[str]) -> list[Chunk]:
        if not symbols:
            return self._sliding_window(file_path, source_lines)
        context = self._build_context(file_path, source_lines)
        merged = self._merge_small(symbols)
        chunks = []
        covered = set()
        for sym in merged:
            for chunk in self._symbol_to_chunks(file_path, sym, source_lines, context):
                chunks.append(chunk)
                for ln in range(chunk.start_line, chunk.end_line + 1):
                    covered.add(ln)
        gap_chunks = self._gap_chunks(file_path, symbols, source_lines, covered, context)
        chunks.extend(gap_chunks)
        return sorted(chunks, key=lambda c: c.start_line)

    def _symbol_to_chunks(self, file_path: str, sym: Symbol, source_lines: list[str], context: str) -> list[Chunk]:
        line_count = sym.end_line - sym.start_line + 1
        if line_count <= self._max_lines:
            content = _lines_to_content(source_lines, sym.start_line, sym.end_line)
            return [Chunk(
                id=_make_id(file_path, sym.start_line, sym.end_line),
                file_path=file_path, start_line=sym.start_line, end_line=sym.end_line,
                content=content, symbol_name=sym.name, symbol_type=sym.type,
                language=sym.language, signature=sym.signature, context=context,
            )]
        return self._split_large(file_path, sym, source_lines, context)

    def _split_large(self, file_path: str, sym: Symbol, source_lines: list[str], context: str) -> list[Chunk]:
        chunks = []
        start = sym.start_line
        while start <= sym.end_line:
            end = min(start + self._max_lines - 1, sym.end_line)
            blank = self._find_blank_split(source_lines, start, end, sym.end_line)
            end = blank if blank else end
            content = _lines_to_content(source_lines, start, end)
            chunks.append(Chunk(
                id=_make_id(file_path, start, end),
                file_path=file_path, start_line=start, end_line=end,
                content=content, symbol_name=sym.name, symbol_type=sym.type,
                language=sym.language, signature=sym.signature, context=context,
            ))
            start = end + 1
        return chunks

    def _find_blank_split(self, source_lines: list[str], start: int, end: int, sym_end: int) -> int | None:
        for i in range(end, start, -1):
            if i <= len(source_lines) and source_lines[i - 1].strip() == "":
                return i
        return None

    def _merge_small(self, symbols: list[Symbol]) -> list[Symbol]:
        if not symbols:
            return []
        result = []
        buffer = [symbols[0]]
        for sym in symbols[1:]:
            total = sum(s.end_line - s.start_line + 1 for s in buffer)
            if total < self._min_lines and sym.start_line == buffer[-1].end_line + 1:
                buffer.append(sym)
            else:
                result.append(self._collapse(buffer))
                buffer = [sym]
        result.append(self._collapse(buffer))
        return result

    def _collapse(self, syms: list[Symbol]) -> Symbol:
        if len(syms) == 1:
            return syms[0]
        from parser import Symbol as Sym
        return Sym(
            name=syms[0].name, type=syms[0].type,
            start_line=syms[0].start_line, end_line=syms[-1].end_line,
            signature=syms[0].signature, body="",
            parent=syms[0].parent, language=syms[0].language,
        )

    def _gap_chunks(self, file_path: str, symbols: list[Symbol], source_lines: list[str], covered: set, context: str) -> list[Chunk]:
        total = len(source_lines)
        chunks = []
        gap_start = None
        for ln in range(1, total + 1):
            if ln not in covered:
                if gap_start is None:
                    gap_start = ln
            else:
                if gap_start is not None:
                    gap_end = ln - 1
                    content = _lines_to_content(source_lines, gap_start, gap_end)
                    if content.strip():
                        chunks.append(Chunk(
                            id=_make_id(file_path, gap_start, gap_end),
                            file_path=file_path, start_line=gap_start, end_line=gap_end,
                            content=content, symbol_name="", symbol_type="module_header",
                            language=symbols[0].language if symbols else "", signature="", context=context,
                        ))
                    gap_start = None
        if gap_start is not None:
            gap_end = total
            content = _lines_to_content(source_lines, gap_start, gap_end)
            if content.strip():
                chunks.append(Chunk(
                    id=_make_id(file_path, gap_start, gap_end),
                    file_path=file_path, start_line=gap_start, end_line=gap_end,
                    content=content, symbol_name="", symbol_type="module_header",
                    language=symbols[0].language if symbols else "", signature="", context=context,
                ))
        return chunks

    def _sliding_window(self, file_path: str, source_lines: list[str]) -> list[Chunk]:
        window, step, total = 100, 50, len(source_lines)
        chunks = []
        start = 1
        while start <= total:
            end = min(start + window - 1, total)
            content = _lines_to_content(source_lines, start, end)
            if content.strip():
                chunks.append(Chunk(
                    id=_make_id(file_path, start, end),
                    file_path=file_path, start_line=start, end_line=end,
                    content=content, symbol_name="", symbol_type="module",
                    language="", signature="", context="",
                ))
            start += step
        return chunks

    def _build_context(self, file_path: str, source_lines: list[str]) -> str:
        parts = [file_path]
        for line in source_lines[:50]:
            stripped = line.strip()
            first_word = stripped.split()[0].lower() if stripped else ""
            if first_word in IMPORT_KEYWORDS:
                parts.append(stripped)
        return "\n".join(parts)
