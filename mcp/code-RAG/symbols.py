import re
import os
import logging
from pathlib import Path
from typing import Optional

logger = logging.getLogger(__name__)

IGNORE_DIRS = {
    "node_modules", ".git", "target", "dist", "build",
    "__pycache__", ".cache", "pkg", "wasm-pack-out",
    ".claude", "venv", ".venv", "env", ".env",
    "runtime", ".idea", ".vscode", ".next",
    "coverage", ".nyc_output", ".turbo",
}

CODE_EXTENSIONS = {".rs", ".ts", ".tsx", ".js", ".jsx", ".vue", ".py"}

TS_PATTERNS = {
    "function": re.compile(
        r'^(?:export\s+)?(?:async\s+)?function\s+(\w+)\s*(?:<[^>]*>)?\s*\(([^)]*)\)(?:\s*:\s*([^\{]+?))?(?:\s*\{|$)',
        re.MULTILINE,
    ),
    "arrow": re.compile(
        r'^(?:export\s+)?(?:const|let|var)\s+(\w+)\s*(?::\s*[^=]+?)?\s*=\s*(?:async\s+)?(?:<[^>]*>)?\s*\(([^)]*)\)\s*(?::\s*([^=]+?))?\s*=>',
        re.MULTILINE,
    ),
    "class": re.compile(
        r'^(?:export\s+)?(?:abstract\s+)?class\s+(\w+)(?:\s+extends\s+(\w+))?(?:\s+implements\s+([^\{]+?))?(?:\s*\{)',
        re.MULTILINE,
    ),
    "interface": re.compile(
        r'^(?:export\s+)?interface\s+(\w+)(?:\s+extends\s+([^\{]+?))?(?:\s*\{)',
        re.MULTILINE,
    ),
    "type_alias": re.compile(
        r'^(?:export\s+)?type\s+(\w+)(?:<[^>]*>)?\s*=\s*(.+?)(?:;|$)',
        re.MULTILINE,
    ),
    "enum": re.compile(
        r'^(?:export\s+)?(?:const\s+)?enum\s+(\w+)',
        re.MULTILINE,
    ),
    "method": re.compile(
        r'^\s+(?:(?:public|private|protected|static|async|readonly|abstract|override|get|set)\s+)*(\w+)\s*(?:<[^>]*>)?\s*\(([^)]*)\)(?:\s*:\s*([^\{;]+?))?(?:\s*[\{;])',
        re.MULTILINE,
    ),
}

RUST_PATTERNS = {
    "function": re.compile(
        r'^(?:\s*(?:pub(?:\([\w:]+\))?\s+)?)?(?:async\s+)?(?:unsafe\s+)?(?:const\s+)?fn\s+(\w+)\s*(?:<[^>]*>)?\s*\(([^)]*)\)(?:\s*->\s*([^\{]+?))?(?:\s*(?:where\s+[^\{]+)?\s*\{)',
        re.MULTILINE,
    ),
    "struct": re.compile(
        r'^(?:pub(?:\([\w:]+\))?\s+)?struct\s+(\w+)(?:<[^>]*>)?',
        re.MULTILINE,
    ),
    "enum": re.compile(
        r'^(?:pub(?:\([\w:]+\))?\s+)?enum\s+(\w+)(?:<[^>]*>)?',
        re.MULTILINE,
    ),
    "trait": re.compile(
        r'^(?:pub(?:\([\w:]+\))?\s+)?(?:unsafe\s+)?trait\s+(\w+)(?:<[^>]*>)?',
        re.MULTILINE,
    ),
    "impl": re.compile(
        r'^impl(?:<[^>]*>)?\s+(?:(\w+)\s+for\s+)?(\w+)(?:<[^>]*>)?',
        re.MULTILINE,
    ),
    "type_alias": re.compile(
        r'^(?:pub(?:\([\w:]+\))?\s+)?type\s+(\w+)(?:<[^>]*>)?\s*=\s*(.+?);',
        re.MULTILINE,
    ),
    "const": re.compile(
        r'^(?:pub(?:\([\w:]+\))?\s+)?(?:const|static)\s+(\w+)\s*:\s*([^=]+?)\s*=',
        re.MULTILINE,
    ),
    "macro": re.compile(
        r'^(?:pub(?:\([\w:]+\))?\s+)?macro_rules!\s+(\w+)',
        re.MULTILINE,
    ),
}

PY_PATTERNS = {
    "function": re.compile(
        r'^(?:async\s+)?def\s+(\w+)\s*\(([^)]*)\)(?:\s*->\s*([^:]+))?:',
        re.MULTILINE,
    ),
    "class": re.compile(
        r'^class\s+(\w+)(?:\(([^)]*)\))?:',
        re.MULTILINE,
    ),
}


def _get_lang(ext: str) -> str:
    return {
        ".rs": "rust", ".ts": "typescript", ".tsx": "typescript",
        ".js": "javascript", ".jsx": "javascript",
        ".vue": "vue", ".py": "python",
    }.get(ext, "")


def extract_symbols(file_path: str, content: str = "") -> list[dict]:
    ext = Path(file_path).suffix
    lang = _get_lang(ext)
    if not lang:
        return []

    if not content:
        try:
            content = Path(file_path).read_text(encoding="utf-8", errors="ignore")
        except Exception:
            return []

    if lang == "vue":
        script_match = re.search(r'<script[^>]*>(.*?)</script>', content, re.DOTALL)
        if script_match:
            content = script_match.group(1)
            lang = "typescript"
        else:
            return []

    lines = content.split("\n")
    symbols = []

    def _line_at(pos):
        return content[:pos].count("\n") + 1

    if lang in ("typescript", "javascript"):
        patterns = TS_PATTERNS
        current_class = None

        for kind, pat in patterns.items():
            for m in pat.finditer(content):
                line = _line_at(m.start())
                name = m.group(1)

                if kind == "function":
                    params = m.group(2).strip()
                    ret = (m.group(3) or "").strip()
                    symbols.append({
                        "name": name, "kind": "function", "line": line,
                        "signature": f"({params})" + (f": {ret}" if ret else ""),
                        "file": file_path, "language": lang,
                    })
                elif kind == "arrow":
                    params = m.group(2).strip()
                    ret = (m.group(3) or "").strip()
                    symbols.append({
                        "name": name, "kind": "function", "line": line,
                        "signature": f"({params})" + (f": {ret}" if ret else ""),
                        "file": file_path, "language": lang,
                    })
                elif kind == "class":
                    extends = m.group(2) or ""
                    symbols.append({
                        "name": name, "kind": "class", "line": line,
                        "signature": f"extends {extends}" if extends else "",
                        "file": file_path, "language": lang,
                    })
                elif kind == "interface":
                    extends = (m.group(2) or "").strip()
                    symbols.append({
                        "name": name, "kind": "interface", "line": line,
                        "signature": f"extends {extends}" if extends else "",
                        "file": file_path, "language": lang,
                    })
                elif kind == "type_alias":
                    value = m.group(2).strip()[:80]
                    symbols.append({
                        "name": name, "kind": "type", "line": line,
                        "signature": f"= {value}",
                        "file": file_path, "language": lang,
                    })
                elif kind == "enum":
                    symbols.append({
                        "name": name, "kind": "enum", "line": line,
                        "signature": "",
                        "file": file_path, "language": lang,
                    })
                elif kind == "method":
                    if name in ("if", "else", "for", "while", "switch", "return", "new", "delete", "typeof", "constructor"):
                        if name != "constructor":
                            continue
                    params = m.group(2).strip()
                    ret = (m.group(3) or "").strip()
                    symbols.append({
                        "name": name, "kind": "method", "line": line,
                        "signature": f"({params})" + (f": {ret}" if ret else ""),
                        "file": file_path, "language": lang,
                    })

    elif lang == "rust":
        for kind, pat in RUST_PATTERNS.items():
            for m in pat.finditer(content):
                line = _line_at(m.start())

                if kind == "function":
                    name = m.group(1)
                    params = m.group(2).strip()
                    ret = (m.group(3) or "").strip()
                    symbols.append({
                        "name": name, "kind": "function", "line": line,
                        "signature": f"({params})" + (f" -> {ret}" if ret else ""),
                        "file": file_path, "language": lang,
                    })
                elif kind in ("struct", "enum", "trait"):
                    name = m.group(1)
                    symbols.append({
                        "name": name, "kind": kind, "line": line,
                        "signature": "",
                        "file": file_path, "language": lang,
                    })
                elif kind == "impl":
                    trait_name = m.group(1) or ""
                    type_name = m.group(2)
                    sig = f"{trait_name} for {type_name}" if trait_name else type_name
                    symbols.append({
                        "name": type_name, "kind": "impl", "line": line,
                        "signature": sig,
                        "file": file_path, "language": lang,
                    })
                elif kind == "type_alias":
                    name = m.group(1)
                    value = m.group(2).strip()[:80]
                    symbols.append({
                        "name": name, "kind": "type", "line": line,
                        "signature": f"= {value}",
                        "file": file_path, "language": lang,
                    })
                elif kind == "const":
                    name = m.group(1)
                    ty = m.group(2).strip()
                    symbols.append({
                        "name": name, "kind": "const", "line": line,
                        "signature": f": {ty}",
                        "file": file_path, "language": lang,
                    })
                elif kind == "macro":
                    name = m.group(1)
                    symbols.append({
                        "name": name, "kind": "macro", "line": line,
                        "signature": "",
                        "file": file_path, "language": lang,
                    })

    elif lang == "python":
        indent_stack = []
        for kind, pat in PY_PATTERNS.items():
            for m in pat.finditer(content):
                line = _line_at(m.start())
                name = m.group(1)

                if kind == "function":
                    params = m.group(2).strip()
                    ret = (m.group(3) or "").strip()
                    symbols.append({
                        "name": name, "kind": "function", "line": line,
                        "signature": f"({params})" + (f" -> {ret}" if ret else ""),
                        "file": file_path, "language": lang,
                    })
                elif kind == "class":
                    bases = (m.group(2) or "").strip()
                    symbols.append({
                        "name": name, "kind": "class", "line": line,
                        "signature": f"({bases})" if bases else "",
                        "file": file_path, "language": lang,
                    })

    return symbols


def collect_all_symbols(project_root: str) -> list[dict]:
    root = Path(project_root)
    all_symbols = []

    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in IGNORE_DIRS]
        for fname in filenames:
            fpath = Path(dirpath) / fname
            if fpath.suffix not in CODE_EXTENSIONS:
                continue
            try:
                if fpath.stat().st_size > 256 * 1024:
                    continue
            except OSError:
                continue

            syms = extract_symbols(str(fpath))
            all_symbols.extend(syms)

    return all_symbols


def find_callers(symbol_name: str, project_root: str, lang_filter: str = "") -> list[dict]:
    root = Path(project_root)
    callers = []

    call_patterns = [
        re.compile(rf'\b{re.escape(symbol_name)}\s*\('),
        re.compile(rf'\b{re.escape(symbol_name)}\s*<[^>]*>\s*\('),
        re.compile(rf'::{re.escape(symbol_name)}\s*\('),
        re.compile(rf'\.{re.escape(symbol_name)}\s*\('),
    ]

    def_patterns = [
        re.compile(rf'^\s*(?:pub\s+)?(?:async\s+)?(?:fn|function|def|const|let|var|class|struct|enum|trait|interface|type)\s+{re.escape(symbol_name)}\b', re.MULTILINE),
        re.compile(rf'^\s*(?:export\s+)?(?:async\s+)?(?:function|class|interface|type|enum|const|let|var)\s+{re.escape(symbol_name)}\b', re.MULTILINE),
    ]

    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in IGNORE_DIRS]
        for fname in filenames:
            fpath = Path(dirpath) / fname
            if fpath.suffix not in CODE_EXTENSIONS:
                continue
            if lang_filter:
                file_lang = _get_lang(fpath.suffix)
                if file_lang != lang_filter:
                    continue
            try:
                content = fpath.read_text(encoding="utf-8", errors="ignore")
            except Exception:
                continue

            for line_num, line in enumerate(content.split("\n"), 1):
                is_def = any(p.search(line) for p in def_patterns)
                if is_def:
                    continue

                for cp in call_patterns:
                    if cp.search(line):
                        callers.append({
                            "file": str(fpath),
                            "line": line_num,
                            "text": line.strip()[:120],
                        })
                        break

    return callers


_IMPL_FOR_RE = re.compile(
    r'^impl(?:<[^>]*>)?\s+(\w+)\s+for\s+(\w+)', re.MULTILINE
)
_IMPL_SELF_RE = re.compile(
    r'^impl(?:<[^>]*>)?\s+(\w+)(?:<[^>]*>)?\s*\{', re.MULTILINE
)
_RUST_DEF_RE = re.compile(
    r'^(?:pub(?:\([^)]*\))?\s+)?(?:struct|enum|trait)\s+(\w+)', re.MULTILINE
)
_RUST_DEF_KIND_RE = re.compile(
    r'^(?:pub(?:\([^)]*\))?\s+)?(struct|enum|trait)\s+(\w+)', re.MULTILINE
)


def get_type_hierarchy(project_root: str) -> dict:
    root = Path(project_root)
    types: dict[str, dict] = {}
    edges: list[dict] = []

    def _ensure_type(name, kind="unknown", file="", line=0):
        if name not in types:
            types[name] = {
                "kind": kind,
                "file": file,
                "line": line,
                "extends": [],
                "implements": [],
                "implemented_by": [],
                "extended_by": [],
            }
        elif kind != "unknown" and types[name]["kind"] == "unknown":
            types[name]["kind"] = kind
            types[name]["file"] = file
            types[name]["line"] = line

    def _line_at(content, pos):
        return content[:pos].count("\n") + 1

    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in IGNORE_DIRS]
        for fname in filenames:
            fpath = Path(dirpath) / fname
            if fpath.suffix not in CODE_EXTENSIONS:
                continue
            try:
                if fpath.stat().st_size > 256 * 1024:
                    continue
            except OSError:
                continue

            try:
                content = fpath.read_text(encoding="utf-8", errors="ignore")
            except Exception:
                continue

            lang = _get_lang(fpath.suffix)
            fstr = str(fpath)

            if lang == "rust":
                for m in _RUST_DEF_KIND_RE.finditer(content):
                    kind = m.group(1)
                    name = m.group(2)
                    _ensure_type(name, kind, fstr, _line_at(content, m.start()))

                for m in _IMPL_FOR_RE.finditer(content):
                    trait_name = m.group(1)
                    type_name = m.group(2)
                    line = _line_at(content, m.start())
                    _ensure_type(type_name)
                    _ensure_type(trait_name, "trait")
                    if trait_name not in types[type_name]["implements"]:
                        types[type_name]["implements"].append(trait_name)
                    edges.append({
                        "from": type_name, "to": trait_name,
                        "relation": "implements", "file": fstr, "line": line,
                    })

            elif lang in ("typescript", "javascript") or (lang == "vue"):
                if lang == "vue":
                    script_match = re.search(r'<script[^>]*>(.*?)</script>', content, re.DOTALL)
                    if script_match:
                        content = script_match.group(1)
                    else:
                        continue

                for m in TS_PATTERNS["class"].finditer(content):
                    name = m.group(1)
                    extends = m.group(2) or ""
                    implements_raw = (m.group(3) or "").strip()
                    line = _line_at(content, m.start())
                    _ensure_type(name, "class", fstr, line)

                    if extends:
                        extends = extends.strip()
                        _ensure_type(extends)
                        if extends not in types[name]["extends"]:
                            types[name]["extends"].append(extends)
                        edges.append({
                            "from": name, "to": extends,
                            "relation": "extends", "file": fstr, "line": line,
                        })

                    if implements_raw:
                        for iface in re.split(r'\s*,\s*', implements_raw):
                            iface = iface.strip().split("<")[0].strip()
                            if not iface:
                                continue
                            _ensure_type(iface, "interface")
                            if iface not in types[name]["implements"]:
                                types[name]["implements"].append(iface)
                            edges.append({
                                "from": name, "to": iface,
                                "relation": "implements", "file": fstr, "line": line,
                            })

                for m in TS_PATTERNS["interface"].finditer(content):
                    name = m.group(1)
                    extends_raw = (m.group(2) or "").strip()
                    line = _line_at(content, m.start())
                    _ensure_type(name, "interface", fstr, line)

                    if extends_raw:
                        for base in re.split(r'\s*,\s*', extends_raw):
                            base = base.strip().split("<")[0].strip()
                            if not base:
                                continue
                            _ensure_type(base, "interface")
                            if base not in types[name]["extends"]:
                                types[name]["extends"].append(base)
                            edges.append({
                                "from": name, "to": base,
                                "relation": "extends", "file": fstr, "line": line,
                            })

                for m in TS_PATTERNS["enum"].finditer(content):
                    name = m.group(1)
                    _ensure_type(name, "enum", fstr, _line_at(content, m.start()))

            elif lang == "python":
                for m in PY_PATTERNS["class"].finditer(content):
                    name = m.group(1)
                    bases = (m.group(2) or "").strip()
                    line = _line_at(content, m.start())
                    _ensure_type(name, "class", fstr, line)

                    if bases:
                        for base in re.split(r'\s*,\s*', bases):
                            base = base.strip().split("(")[0].strip()
                            if not base or base in ("object",):
                                continue
                            _ensure_type(base)
                            if base not in types[name]["extends"]:
                                types[name]["extends"].append(base)
                            edges.append({
                                "from": name, "to": base,
                                "relation": "extends", "file": fstr, "line": line,
                            })

    for name, info in types.items():
        for parent in info["extends"]:
            if parent in types:
                if name not in types[parent]["extended_by"]:
                    types[parent]["extended_by"].append(name)
        for trait in info["implements"]:
            if trait in types:
                if name not in types[trait]["implemented_by"]:
                    types[trait]["implemented_by"].append(name)

    return {"types": types, "edges": edges}


_SKIP_NAMES = {
    "main", "new", "constructor", "init", "setup", "teardown",
    "default", "from", "into", "drop", "clone", "fmt",
    "eq", "ne", "partial_cmp", "cmp", "hash",
    "deref", "deref_mut", "index", "index_mut",
    "next", "size_hint", "len", "is_empty",
    "serialize", "deserialize",
}


def find_dead_code(project_root: str, language: str = "") -> list[dict]:
    root = Path(project_root)
    all_symbols = collect_all_symbols(project_root)

    trait_methods: set[str] = set()
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in IGNORE_DIRS]
        for fname in filenames:
            fpath = Path(dirpath) / fname
            if fpath.suffix != ".rs":
                continue
            try:
                if fpath.stat().st_size > 256 * 1024:
                    continue
                content = fpath.read_text(encoding="utf-8", errors="ignore")
            except Exception:
                continue
            in_trait = False
            brace_depth = 0
            for line in content.split("\n"):
                stripped = line.strip()
                if re.match(r'^(?:pub(?:\([^)]*\))?\s+)?(?:unsafe\s+)?trait\s+', stripped):
                    in_trait = True
                    brace_depth = 0
                if in_trait:
                    brace_depth += line.count("{") - line.count("}")
                    fn_match = re.match(r'^\s*(?:async\s+)?fn\s+(\w+)', line)
                    if fn_match:
                        trait_methods.add(fn_match.group(1))
                    if brace_depth <= 0 and in_trait:
                        in_trait = False

    file_contents: dict[str, str] = {}
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in IGNORE_DIRS]
        for fname in filenames:
            fpath = Path(dirpath) / fname
            if fpath.suffix not in CODE_EXTENSIONS:
                continue
            if language:
                if _get_lang(fpath.suffix) != language:
                    continue
            try:
                if fpath.stat().st_size > 256 * 1024:
                    continue
                file_contents[str(fpath)] = fpath.read_text(encoding="utf-8", errors="ignore")
            except Exception:
                continue

    name_pattern_cache: dict[str, re.Pattern] = {}
    dead: list[dict] = []

    for sym in all_symbols:
        if sym["kind"] not in ("function", "method"):
            continue
        if language and sym.get("language", "") != language:
            continue

        name = sym["name"]
        if name in _SKIP_NAMES:
            continue
        if name.startswith("_"):
            continue
        if name.startswith("test_"):
            continue
        if name in trait_methods and sym.get("language") == "rust":
            continue

        sym_file = sym["file"]
        sym_line = sym["line"]

        try:
            src_lines = file_contents.get(sym_file, "").split("\n")
            if sym_line > 0 and sym_line <= len(src_lines):
                prev_line = src_lines[sym_line - 2].strip() if sym_line >= 2 else ""
                if "#[wasm_bindgen" in prev_line or "#[test" in prev_line:
                    continue
                if "export" in src_lines[sym_line - 1]:
                    continue
        except Exception:
            pass

        if name not in name_pattern_cache:
            name_pattern_cache[name] = re.compile(rf'\b{re.escape(name)}\b')

        pat = name_pattern_cache[name]
        found_elsewhere = False

        for fpath_str, content in file_contents.items():
            for line_num, line in enumerate(content.split("\n"), 1):
                if not pat.search(line):
                    continue
                if fpath_str == sym_file and line_num == sym_line:
                    continue
                found_elsewhere = True
                break
            if found_elsewhere:
                break

        if not found_elsewhere:
            dead.append({
                "name": name,
                "kind": sym["kind"],
                "file": sym_file,
                "line": sym_line,
                "language": sym.get("language", ""),
            })

    return dead


_DEF_KW_RE = re.compile(
    r'^\s*(?:export\s+)?(?:pub(?:\([^)]*\))?\s+)?'
    r'(?:async\s+)?(?:unsafe\s+)?(?:const\s+)?'
    r'(?:fn|function|def|class|struct|enum|trait|interface|type|macro_rules!)\s+'
)
_IMPORT_RE = re.compile(r'\b(?:import|from|use|require)\b')
_CALL_RE_TMPL = r'(?:^|[.\s:]){}(\s*(?:<[^>]*>\s*)?\()'
_TYPE_REF_CONTEXT = re.compile(r'(?::\s*$|->|<\s*$|\bextends\b|\bimplements\b|\bwhere\b)')
_STRING_CHAR = {'"', "'", '`'}


def preview_rename(old_name: str, new_name: str, project_root: str, language: str = "") -> list[dict]:
    root = Path(project_root)
    word_re = re.compile(rf'\b{re.escape(old_name)}\b')
    results: list[dict] = []

    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in IGNORE_DIRS]
        for fname in filenames:
            fpath = Path(dirpath) / fname
            if fpath.suffix not in CODE_EXTENSIONS:
                continue
            if language:
                if _get_lang(fpath.suffix) != language:
                    continue
            try:
                if fpath.stat().st_size > 256 * 1024:
                    continue
                content = fpath.read_text(encoding="utf-8", errors="ignore")
            except Exception:
                continue

            fstr = str(fpath)

            for line_num, line in enumerate(content.split("\n"), 1):
                for m in word_re.finditer(line):
                    col = m.start()
                    text = line.strip()[:120]

                    in_string = False
                    quote_char = None
                    i = 0
                    while i < col:
                        ch = line[i]
                        if ch == '\\' and quote_char:
                            i += 2
                            continue
                        if ch in _STRING_CHAR:
                            if not in_string:
                                in_string = True
                                quote_char = ch
                            elif ch == quote_char:
                                in_string = False
                                quote_char = None
                        i += 1

                    stripped = line.lstrip()
                    is_comment = (
                        stripped.startswith("//")
                        or stripped.startswith("#")
                        or stripped.startswith("*")
                        or stripped.startswith("/*")
                    )

                    if in_string or is_comment:
                        results.append({
                            "file": fstr, "line": line_num, "column": col,
                            "text": text,
                            "category": "string_literal" if in_string else "comment",
                            "would_rename": False,
                        })
                        continue

                    category = "other"
                    if _DEF_KW_RE.match(line) and old_name in line[line.find(old_name):line.find(old_name)+len(old_name)+1]:
                        category = "definition"
                    elif _IMPORT_RE.search(line):
                        category = "import"
                    elif re.search(rf'(?:\.|::){re.escape(old_name)}\s*\(', line) or re.search(rf'\b{re.escape(old_name)}\s*(?:<[^>]*>\s*)?\(', line):
                        category = "call"
                    else:
                        before = line[:col].rstrip()
                        if before.endswith(":") or before.endswith("->") or before.endswith("<") or "extends" in line or "implements" in line or "where" in line:
                            category = "type_reference"

                    results.append({
                        "file": fstr, "line": line_num, "column": col,
                        "text": text,
                        "category": category,
                        "would_rename": True,
                    })

    return results
