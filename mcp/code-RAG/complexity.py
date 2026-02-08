import re
import os
from pathlib import Path
from symbols import IGNORE_DIRS, CODE_EXTENSIONS


def _ext_to_lang(ext: str) -> str:
    return {
        ".rs": "rust", ".ts": "typescript", ".tsx": "typescript",
        ".js": "javascript", ".jsx": "javascript",
        ".vue": "vue", ".py": "python",
    }.get(ext, "")


def _extract_balanced_braces(content: str, start: int) -> tuple[int, str]:
    depth = 0
    i = start
    while i < len(content) and content[i] != '{':
        i += 1
    if i >= len(content):
        return start, ""
    body_start = i
    while i < len(content):
        if content[i] == '{':
            depth += 1
        elif content[i] == '}':
            depth -= 1
            if depth == 0:
                return i + 1, content[body_start:i + 1]
        i += 1
    return i, content[body_start:i]


def _extract_function_bodies(content: str, language: str) -> list[tuple[str, int, str]]:
    results = []

    if language == "rust":
        pat = re.compile(
            r'^(?:\s*(?:pub(?:\([\w:]+\))?\s+)?)?(?:async\s+)?(?:unsafe\s+)?(?:const\s+)?fn\s+(\w+)\s*(?:<[^>]*>)?\s*\([^)]*\)',
            re.MULTILINE,
        )
        for m in pat.finditer(content):
            name = m.group(1)
            line = content[:m.start()].count("\n") + 1
            end_pos, body = _extract_balanced_braces(content, m.end())
            if body:
                results.append((name, line, body))

    elif language in ("typescript", "javascript"):
        func_pat = re.compile(
            r'(?:export\s+)?(?:async\s+)?function\s+(\w+)\s*(?:<[^>]*>)?\s*\([^)]*\)',
            re.MULTILINE,
        )
        for m in func_pat.finditer(content):
            name = m.group(1)
            line = content[:m.start()].count("\n") + 1
            end_pos, body = _extract_balanced_braces(content, m.end())
            if body:
                results.append((name, line, body))

        arrow_pat = re.compile(
            r'(?:export\s+)?(?:const|let|var)\s+(\w+)\s*(?::[^=]+?)?\s*=\s*(?:async\s+)?(?:<[^>]*>)?\s*\([^)]*\)\s*(?::[^=]+?)?\s*=>',
            re.MULTILINE,
        )
        for m in arrow_pat.finditer(content):
            name = m.group(1)
            line = content[:m.start()].count("\n") + 1
            end_pos, body = _extract_balanced_braces(content, m.end())
            if body:
                results.append((name, line, body))

        method_pat = re.compile(
            r'^\s+(?:(?:public|private|protected|static|async|readonly|abstract|override|get|set)\s+)*(\w+)\s*(?:<[^>]*>)?\s*\([^)]*\)\s*(?::[^{;]+?)?\s*\{',
            re.MULTILINE,
        )
        skip_keywords = {"if", "else", "for", "while", "switch", "return", "new", "delete", "typeof"}
        for m in method_pat.finditer(content):
            name = m.group(1)
            if name in skip_keywords:
                continue
            line = content[:m.start()].count("\n") + 1
            brace_pos = m.end() - 1
            end_pos, body = _extract_balanced_braces(content, brace_pos)
            if body:
                results.append((name, line, body))

    elif language == "python":
        pat = re.compile(r'^( *)(?:async\s+)?def\s+(\w+)\s*\([^)]*\)[^:]*:', re.MULTILINE)
        lines = content.split("\n")
        for m in pat.finditer(content):
            name = m.group(2)
            base_indent = len(m.group(1))
            start_line = content[:m.start()].count("\n") + 1
            start_line_idx = start_line - 1
            body_lines = []
            for i in range(start_line_idx + 1, len(lines)):
                ln = lines[i]
                if ln.strip() == "":
                    body_lines.append(ln)
                    continue
                indent = len(ln) - len(ln.lstrip())
                if indent > base_indent:
                    body_lines.append(ln)
                else:
                    break
            while body_lines and body_lines[-1].strip() == "":
                body_lines.pop()
            if body_lines:
                results.append((name, start_line, "\n".join(body_lines)))

    return results


def _compute_complexity_rust(body: str) -> int:
    c = 1
    c += len(re.findall(r'\bif\b', body))
    c += len(re.findall(r'\belse\s+if\b', body))
    c += len(re.findall(r'\bfor\b', body))
    c += len(re.findall(r'\bwhile\b', body))
    c += len(re.findall(r'\bloop\b', body))
    c += len(re.findall(r'=>', body))
    c += len(re.findall(r'&&', body))
    c += len(re.findall(r'\|\|', body))
    c += len(re.findall(r'\?', body))
    c += len(re.findall(r'\.unwrap\(\)', body))
    return c


def _compute_complexity_ts(body: str) -> int:
    c = 1
    c += len(re.findall(r'\bif\b', body))
    c += len(re.findall(r'\belse\s+if\b', body))
    c += len(re.findall(r'\bfor\b', body))
    c += len(re.findall(r'\bwhile\b', body))
    c += len(re.findall(r'\bcase\b', body))
    c += len(re.findall(r'&&', body))
    c += len(re.findall(r'\|\|', body))
    c += len(re.findall(r'\?(?![.?])', body))
    c += len(re.findall(r'\bcatch\b', body))
    return c


def _compute_complexity_python(body: str) -> int:
    c = 1
    c += len(re.findall(r'\bif\b', body))
    c += len(re.findall(r'\belif\b', body))
    c += len(re.findall(r'\bfor\b', body))
    c += len(re.findall(r'\bwhile\b', body))
    c += len(re.findall(r'\bexcept\b', body))
    c += len(re.findall(r'\band\b', body))
    c += len(re.findall(r'\bor\b', body))
    return c


def _max_nesting_braces(body: str) -> int:
    depth = 0
    max_depth = 0
    for ch in body:
        if ch == '{':
            depth += 1
            max_depth = max(max_depth, depth)
        elif ch == '}':
            depth -= 1
    return max_depth


def _max_nesting_indent(body: str) -> int:
    if not body.strip():
        return 0
    lines = body.split("\n")
    non_empty = [ln for ln in lines if ln.strip()]
    if not non_empty:
        return 0
    base_indent = len(non_empty[0]) - len(non_empty[0].lstrip())
    max_depth = 0
    for ln in non_empty:
        indent = len(ln) - len(ln.lstrip())
        rel = (indent - base_indent) // 4
        if rel > max_depth:
            max_depth = rel
    return max_depth


def compute_complexity(file_path: str) -> list[dict]:
    ext = Path(file_path).suffix
    lang = _ext_to_lang(ext)
    if not lang:
        return []

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

    functions = _extract_function_bodies(content, lang)
    results = []

    for name, line, body in functions:
        if lang == "rust":
            cx = _compute_complexity_rust(body)
            nd = _max_nesting_braces(body)
        elif lang in ("typescript", "javascript"):
            cx = _compute_complexity_ts(body)
            nd = _max_nesting_braces(body)
        elif lang == "python":
            cx = _compute_complexity_python(body)
            nd = _max_nesting_indent(body)
        else:
            continue

        body_lines = body.count("\n") + 1
        results.append({
            "name": name,
            "file": file_path,
            "line": line,
            "complexity": cx,
            "nesting_depth": nd,
            "lines": body_lines,
        })

    return results


def find_hotspots(directory: str, top_n: int = 30) -> list[dict]:
    root = Path(directory)
    all_funcs = []

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

            lang = _ext_to_lang(fpath.suffix)
            if not lang:
                continue

            metrics = compute_complexity(str(fpath))
            for m in metrics:
                m["language"] = lang
                all_funcs.append(m)

    all_funcs.sort(key=lambda x: x["complexity"], reverse=True)
    return all_funcs[:top_n]
