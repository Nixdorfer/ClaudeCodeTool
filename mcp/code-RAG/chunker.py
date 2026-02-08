from __future__ import annotations
import re
from typing import Optional

try:
    from tree_sitter_languages import get_parser
    HAS_TREE_SITTER = True
except ImportError:
    HAS_TREE_SITTER = False

_TS_LANG_MAP = {
    "rust": "rust", "typescript": "typescript", "javascript": "javascript",
    "python": "python", "c": "c", "cpp": "cpp", "csharp": "c_sharp",
    "go": "go", "php": "php", "vue": "javascript",
}

_FUNC_NODE_TYPES = {
    "rust": {"function_item", "impl_item", "trait_item", "struct_item", "enum_item"},
    "typescript": {"function_declaration", "method_definition", "class_declaration",
                    "interface_declaration", "type_alias_declaration", "enum_declaration"},
    "javascript": {"function_declaration", "method_definition", "class_declaration"},
    "python": {"function_definition", "class_definition"},
    "c": {"function_definition", "struct_specifier", "enum_specifier"},
    "cpp": {"function_definition", "class_specifier", "struct_specifier",
            "enum_specifier", "namespace_definition"},
    "c_sharp": {"method_declaration", "class_declaration", "struct_declaration",
                "interface_declaration", "enum_declaration", "namespace_declaration"},
    "go": {"function_declaration", "method_declaration", "type_declaration"},
    "php": {"function_definition", "method_declaration", "class_declaration",
            "interface_declaration", "trait_declaration"},
}

_TOP_LEVEL_CONTAINERS = {
    "impl_item", "class_declaration", "class_definition", "class_specifier",
    "struct_specifier", "namespace_definition", "namespace_declaration",
    "interface_declaration", "trait_item", "trait_declaration",
    "module", "program",
}

MIN_CHUNK_LINES = 3
MAX_CHUNK_LINES = 120
GLUE_THRESHOLD = 8


def _get_name(node) -> str:
    for child in node.children:
        if child.type in ("identifier", "name", "type_identifier", "property_identifier"):
            return child.text.decode("utf-8", errors="replace")
    return ""


def _node_text(node, source_bytes: bytes) -> str:
    return source_bytes[node.start_byte:node.end_byte].decode("utf-8", errors="replace")


def chunk_by_functions(source: str, language: str) -> list[dict]:
    ts_lang = _TS_LANG_MAP.get(language)
    if not HAS_TREE_SITTER or not ts_lang:
        return _chunk_by_lines_fallback(source, language)

    try:
        parser = get_parser(ts_lang)
    except Exception:
        return _chunk_by_lines_fallback(source, language)

    source_bytes = source.encode("utf-8")
    tree = parser.parse(source_bytes)

    func_types = _FUNC_NODE_TYPES.get(ts_lang, set())
    chunks: list[dict] = []
    covered = set()

    def visit(node, depth=0):
        if node.type in func_types:
            start_line = node.start_point[0] + 1
            end_line = node.end_point[0] + 1
            line_count = end_line - start_line + 1

            if line_count > MAX_CHUNK_LINES and node.type in _TOP_LEVEL_CONTAINERS:
                for child in node.children:
                    visit(child, depth + 1)
                return

            text = _node_text(node, source_bytes)
            name = _get_name(node)
            chunks.append({
                "start_line": start_line,
                "end_line": end_line,
                "content": text,
                "name": name,
                "kind": node.type,
            })
            for line in range(start_line, end_line + 1):
                covered.add(line)
            return

        for child in node.children:
            visit(child, depth + 1)

    visit(tree.root_node)

    lines = source.split("\n")
    gap_start = None
    for i in range(1, len(lines) + 1):
        if i not in covered:
            if gap_start is None:
                gap_start = i
        else:
            if gap_start is not None and (i - gap_start) >= GLUE_THRESHOLD:
                gap_text = "\n".join(lines[gap_start - 1:i - 1])
                if gap_text.strip():
                    chunks.append({
                        "start_line": gap_start,
                        "end_line": i - 1,
                        "content": gap_text,
                        "name": "",
                        "kind": "gap",
                    })
                gap_start = None
            elif gap_start is not None:
                gap_start = None

    if gap_start is not None and (len(lines) + 1 - gap_start) >= GLUE_THRESHOLD:
        gap_text = "\n".join(lines[gap_start - 1:])
        if gap_text.strip():
            chunks.append({
                "start_line": gap_start,
                "end_line": len(lines),
                "content": gap_text,
                "name": "",
                "kind": "gap",
            })

    if not chunks:
        return _chunk_by_lines_fallback(source, language)

    chunks.sort(key=lambda c: c["start_line"])
    return chunks


def get_function_body(source: str, language: str, function_name: str) -> Optional[dict]:
    ts_lang = _TS_LANG_MAP.get(language)
    if not HAS_TREE_SITTER or not ts_lang:
        return _regex_find_function(source, language, function_name)

    try:
        parser = get_parser(ts_lang)
    except Exception:
        return _regex_find_function(source, language, function_name)

    source_bytes = source.encode("utf-8")
    tree = parser.parse(source_bytes)
    func_types = _FUNC_NODE_TYPES.get(ts_lang, set())
    matches = []

    def visit(node):
        if node.type in func_types:
            name = _get_name(node)
            if name == function_name:
                matches.append({
                    "name": name,
                    "kind": node.type,
                    "start_line": node.start_point[0] + 1,
                    "end_line": node.end_point[0] + 1,
                    "content": _node_text(node, source_bytes),
                })
        for child in node.children:
            visit(child)

    visit(tree.root_node)
    return matches[0] if matches else None


def _chunk_by_lines_fallback(source: str, language: str, chunk_lines: int = 60, overlap: int = 10) -> list[dict]:
    lines = source.split("\n")
    if len(lines) <= chunk_lines:
        return [{"start_line": 1, "end_line": len(lines), "content": source, "name": "", "kind": "block"}]
    chunks = []
    step = chunk_lines - overlap
    for i in range(0, len(lines), step):
        end = min(i + chunk_lines, len(lines))
        chunk = "\n".join(lines[i:end])
        chunks.append({"start_line": i + 1, "end_line": end, "content": chunk, "name": "", "kind": "block"})
        if end >= len(lines):
            break
    return chunks


def _regex_find_function(source: str, language: str, function_name: str) -> Optional[dict]:
    patterns = {
        "rust": rf'^\s*(pub\s+)?(async\s+)?fn\s+{re.escape(function_name)}\s*',
        "typescript": rf'(?:export\s+)?(?:async\s+)?function\s+{re.escape(function_name)}\s*[<(]',
        "javascript": rf'(?:export\s+)?(?:async\s+)?function\s+{re.escape(function_name)}\s*\(',
        "python": rf'^\s*(?:async\s+)?def\s+{re.escape(function_name)}\s*\(',
        "c": rf'[\w*&\s]+\b{re.escape(function_name)}\s*\(',
        "cpp": rf'[\w*&:<>\s]+\b{re.escape(function_name)}\s*\(',
        "csharp": rf'[\w<>\[\],\s]+\s+{re.escape(function_name)}\s*\(',
        "go": rf'func\s+(?:\(\w+\s+\*?\w+\)\s+)?{re.escape(function_name)}\s*\(',
        "php": rf'function\s+{re.escape(function_name)}\s*\(',
    }
    pattern = patterns.get(language)
    if not pattern:
        return None

    lines = source.split("\n")
    for i, line in enumerate(lines):
        if re.search(pattern, line):
            end = _find_block_end(lines, i, language)
            content = "\n".join(lines[i:end + 1])
            return {
                "name": function_name,
                "kind": "function",
                "start_line": i + 1,
                "end_line": end + 1,
                "content": content,
            }
    return None


def _find_block_end(lines: list[str], start: int, language: str) -> int:
    if language == "python":
        base_indent = len(lines[start]) - len(lines[start].lstrip())
        for i in range(start + 1, len(lines)):
            stripped = lines[i].strip()
            if not stripped:
                continue
            indent = len(lines[i]) - len(lines[i].lstrip())
            if indent <= base_indent:
                return i - 1
        return len(lines) - 1

    depth = 0
    found_open = False
    for i in range(start, len(lines)):
        for ch in lines[i]:
            if ch == '{':
                depth += 1
                found_open = True
            elif ch == '}':
                depth -= 1
                if found_open and depth == 0:
                    return i
    return min(start + 50, len(lines) - 1)
