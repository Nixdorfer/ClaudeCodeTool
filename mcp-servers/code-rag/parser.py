from dataclasses import dataclass
from pathlib import Path

LANG_MAP = {
    ".go": "go", ".php": "php", ".java": "java", ".rs": "rust",
    ".js": "javascript", ".ts": "typescript", ".html": "html",
    ".vue": "html", ".css": "css", ".sql": "sql",
    ".json": "json", ".yaml": "yaml", ".yml": "yaml", ".toml": "toml",
}

MODULE_ONLY_LANGS = {"json", "yaml", "toml", "css", "sql", "html"}

GO_NODES = {"function_declaration", "method_declaration", "type_declaration"}
PHP_NODES = {"function_definition", "method_declaration", "class_declaration", "interface_declaration"}
JAVA_NODES = {"method_declaration", "class_declaration", "interface_declaration"}
RUST_NODES = {"function_item", "struct_item", "trait_item", "impl_item"}
JS_NODES = {"function_declaration", "arrow_function", "method_definition", "class_declaration"}
TS_NODES = JS_NODES | {"interface_declaration"}

LANG_NODES: dict[str, set[str]] = {
    "go": GO_NODES, "php": PHP_NODES, "java": JAVA_NODES,
    "rust": RUST_NODES, "javascript": JS_NODES, "typescript": TS_NODES,
}


@dataclass
class Symbol:
    name: str
    type: str
    start_line: int
    end_line: int
    signature: str
    body: str
    parent: str | None
    language: str


def _node_text(node, source_bytes: bytes) -> str:
    return source_bytes[node.start_byte:node.end_byte].decode("utf-8", errors="replace")


def _first_line(node, source_bytes: bytes) -> str:
    text = _node_text(node, source_bytes)
    return text.split("\n")[0][:200]


def _get_name(node, source_bytes: bytes, lang: str) -> str:
    name_node = node.child_by_field_name("name")
    if name_node:
        return _node_text(name_node, source_bytes)
    if lang in ("javascript", "typescript") and node.type == "arrow_function":
        parent = node.parent
        if parent and parent.type == "variable_declarator":
            n = parent.child_by_field_name("name")
            if n:
                return _node_text(n, source_bytes)
    return "<anonymous>"


def _node_sym_type(node_type: str) -> str:
    mapping = {
        "function_declaration": "function", "function_definition": "function",
        "function_item": "function", "method_declaration": "method",
        "method_definition": "method", "arrow_function": "function",
        "class_declaration": "class", "interface_declaration": "interface",
        "struct_item": "struct", "trait_item": "trait", "impl_item": "impl",
        "type_declaration": "type",
    }
    return mapping.get(node_type, node_type)


class CodeParser:
    def __init__(self):
        self._parsers: dict[str, object] = {}

    def _get_parser(self, lang: str):
        if lang not in self._parsers:
            from tree_sitter_languages import get_parser
            self._parsers[lang] = get_parser(lang)
        return self._parsers[lang]

    def parse_file(self, file_path: str | Path) -> list[Symbol]:
        file_path = Path(file_path)
        suffix = file_path.suffix.lower()
        lang = LANG_MAP.get(suffix)
        if lang is None:
            return []
        source = file_path.read_bytes()
        source_text = source.decode("utf-8", errors="replace")
        if lang in MODULE_ONLY_LANGS:
            return [Symbol(
                name=file_path.name, type="module", start_line=1,
                end_line=len(source_text.splitlines()),
                signature=file_path.name, body=source_text,
                parent=None, language=lang,
            )]
        if suffix == ".vue":
            return self._parse_vue(source_text, file_path)
        parser = self._get_parser(lang)
        tree = parser.parse(source)
        return self._extract_symbols(tree.root_node, source, lang, None)

    def _parse_vue(self, source_text: str, file_path: str | Path) -> list[Symbol]:
        file_path = Path(file_path)
        parser = self._get_parser("html")
        source_bytes = source_text.encode("utf-8")
        tree = parser.parse(source_bytes)
        script_nodes = []
        self._find_script(tree.root_node, source_bytes, script_nodes)
        if not script_nodes:
            return [Symbol(
                name=file_path.name, type="module", start_line=1,
                end_line=len(source_text.splitlines()),
                signature=file_path.name, body=source_text,
                parent=None, language="html",
            )]
        symbols = []
        for script_content, offset_line in script_nodes:
            js_parser = self._get_parser("javascript")
            js_bytes = script_content.encode("utf-8")
            js_tree = js_parser.parse(js_bytes)
            for sym in self._extract_symbols(js_tree.root_node, js_bytes, "javascript", None):
                symbols.append(Symbol(
                    name=sym.name, type=sym.type,
                    start_line=sym.start_line + offset_line,
                    end_line=sym.end_line + offset_line,
                    signature=sym.signature, body=sym.body,
                    parent=sym.parent, language="javascript",
                ))
        return symbols

    def _find_script(self, node, source_bytes: bytes, result: list):
        if node.type == "script_element":
            start = node.start_point[0]
            text = _node_text(node, source_bytes)
            inner = "\n".join(text.split("\n")[1:-1])
            result.append((inner, start + 1))
        for child in node.children:
            self._find_script(child, source_bytes, result)

    def _extract_symbols(self, node, source_bytes: bytes, lang: str, parent: str | None) -> list[Symbol]:
        symbols = []
        target_types = LANG_NODES.get(lang, set())
        for child in node.children:
            if child.type in target_types:
                name = _get_name(child, source_bytes, lang)
                sym_type = _node_sym_type(child.type)
                body = _node_text(child, source_bytes)
                sig = _first_line(child, source_bytes)
                sym = Symbol(
                    name=name, type=sym_type,
                    start_line=child.start_point[0] + 1,
                    end_line=child.end_point[0] + 1,
                    signature=sig, body=body,
                    parent=parent, language=lang,
                )
                symbols.append(sym)
                if child.type in ("class_declaration", "impl_item", "trait_item"):
                    symbols.extend(self._extract_symbols(child, source_bytes, lang, name))
            else:
                symbols.extend(self._extract_symbols(child, source_bytes, lang, parent))
        return symbols
