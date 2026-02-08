import os
import sys
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed

logging.basicConfig(
    level=logging.WARNING,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stderr)],
)
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("httpcore").setLevel(logging.WARNING)
logging.getLogger("sentence_transformers").setLevel(logging.WARNING)
logging.getLogger("huggingface_hub").setLevel(logging.WARNING)
logger = logging.getLogger("code-rag")
logger.setLevel(logging.INFO)

from sentence_transformers import SentenceTransformer
from mcp.server.fastmcp import FastMCP
from rag_engine import RAGEngine, summarize_chunk
from lang_registry import ext_to_lang
from file_walker import init_config, get_lib_dirs
from analysis import (
    get_dependency_graph as _get_dep_graph,
    find_similar_code as _find_similar,
    trace_cross_language as _trace_cross_lang,
)
from symbols import (
    collect_all_symbols,
    find_callers as _find_callers,
    get_type_hierarchy as _get_type_hierarchy,
    preview_rename as _preview_rename,
)
from structure import (
    file_summary as _file_summary,
    module_map as _module_map,
    format_module_map as _format_module_map,
)

PROJECT_ROOT = os.environ.get("PROJECT_ROOT") or os.getcwd()
PROJECT_DB = os.environ.get("RAG_DB_PATH") or os.path.join(PROJECT_ROOT, ".claude", "mcp", "code-RAG")
GLOBAL_DB = os.path.join(os.path.expanduser("~"), ".claude", "mcp", "code-RAG", "global_kb")
MODEL_NAME = os.environ.get("RAG_MODEL", "all-MiniLM-L6-v2")

os.makedirs(PROJECT_DB, exist_ok=True)
os.makedirs(GLOBAL_DB, exist_ok=True)

init_config(PROJECT_ROOT)

shared_model = SentenceTransformer(MODEL_NAME)
project_engine = RAGEngine(db_path=PROJECT_DB, model=shared_model)
global_engine = RAGEngine(db_path=GLOBAL_DB, model=shared_model)

lib_engines: dict[str, RAGEngine] = {}
for _lib_rel in get_lib_dirs():
    _lib_name = _lib_rel.replace("/", "_").replace("\\", "_").strip("_")
    _lib_db = os.path.join(PROJECT_DB, "libs", _lib_name)
    os.makedirs(_lib_db, exist_ok=True)
    lib_engines[_lib_rel] = RAGEngine(db_path=_lib_db, model=shared_model)
    logger.info(f"Lib engine created: {_lib_rel} -> {_lib_db}")

mcp = FastMCP(
    "code-RAG",
    instructions=(
        "Prefer search_code over Glob/Grep for open-ended code searches.\n"
        "After each code change: index_codebase + log to PROJECT_ROOT/.claude/plans/changes.md.\n"
        "Do NOT add_knowledge until user confirms task complete. See skill:code-RAG knowledge.md for full workflow."
    ),
)

logger.info(f"code-RAG started | project={PROJECT_ROOT} | project_db={PROJECT_DB} | global_db={GLOBAL_DB} | libs={list(lib_engines.keys())}")


def _format_knowledge_results(results: list[dict], label: str) -> list[str]:
    if not results:
        return []
    lines = []
    for k in results:
        tags_str = ", ".join(k["tags"]) if k["tags"] else ""
        lines.append(
            f"  [{k['category']}] {k['title']} (score: {k['score']:.1%}){' | ' + tags_str if tags_str else ''}\n"
            f"  {k['content']}"
        )
    return [f"=== {label} ===\n" + "\n\n".join(lines)]


def _resolve_lib_engine(lib: str) -> tuple[str, RAGEngine] | None:
    if lib in lib_engines:
        return lib, lib_engines[lib]
    for key, engine in lib_engines.items():
        if key.split("/")[-1] == lib or key.split("\\")[-1] == lib:
            return key, engine
    return None


def _index_lib(lib_key: str, engine: RAGEngine) -> tuple[str, dict | str]:
    lib_abs = os.path.normpath(os.path.join(PROJECT_ROOT, lib_key))
    if not os.path.isdir(lib_abs):
        return lib_key, f"directory not found: {lib_abs}"
    logger.info(f"Indexing lib: {lib_key} -> {lib_abs}")
    return lib_key, engine.index_directory(lib_abs)


def _index_main(target: str) -> dict:
    result = project_engine.index_directory(target)
    symbols = collect_all_symbols(target)
    sym_result = project_engine.index_symbols(symbols)
    result["symbols_indexed"] = sym_result["indexed"]
    return result


@mcp.tool()
def index_codebase(directory: str = "", lib: str = "") -> str:
    if lib:
        resolved = _resolve_lib_engine(lib)
        if not resolved:
            available = ", ".join(lib_engines.keys()) if lib_engines else "(none)"
            return f"Error: lib '{lib}' not found. Available: {available}"
        lib_key, engine = resolved
        lib_key, result = _index_lib(lib_key, engine)
        if isinstance(result, str):
            return f"Error: {result}"
        return (
            f"Lib '{lib_key}' indexing complete:\n"
            f"  Total files scanned: {result['total_files']}\n"
            f"  Files indexed (new/changed): {result['indexed']}\n"
            f"  Files skipped (unchanged): {result['skipped_unchanged']}\n"
            f"  Chunks created: {result['chunks_created']}"
        )

    target = directory if directory else PROJECT_ROOT
    if not os.path.isdir(target):
        return f"Error: directory not found: {target}"

    futures = {}
    with ThreadPoolExecutor(max_workers=max(1, len(lib_engines) + 1)) as pool:
        futures["__main__"] = pool.submit(_index_main, target)
        for lib_key, engine in lib_engines.items():
            futures[lib_key] = pool.submit(_index_lib, lib_key, engine)

        lines = []
        for key, future in futures.items():
            try:
                r = future.result()
            except Exception as e:
                lines.append(f"[{key}] Error: {e}")
                continue

            if key == "__main__":
                lines.insert(0,
                    f"[main] files={r['total_files']} indexed={r['indexed']} "
                    f"skipped={r['skipped_unchanged']} chunks={r['chunks_created']} "
                    f"symbols={r['symbols_indexed']}"
                )
            else:
                lib_name, lib_result = r
                if isinstance(lib_result, str):
                    lines.append(f"[{lib_name}] Error: {lib_result}")
                else:
                    lines.append(
                        f"[{lib_name}] files={lib_result['total_files']} indexed={lib_result['indexed']} "
                        f"skipped={lib_result['skipped_unchanged']} chunks={lib_result['chunks_created']}"
                    )

    return "Indexing complete:\n" + "\n".join(lines)


@mcp.tool()
def search_code(query: str, top_k: int = 10, language: str = "", lib: str = "", scope: str = "main") -> str:
    top_k = max(1, min(30, top_k))
    lang = language if language else None

    output_parts = []

    if lib:
        resolved = _resolve_lib_engine(lib)
        if not resolved:
            available = ", ".join(lib_engines.keys()) if lib_engines else "(none)"
            return f"Error: lib '{lib}' not found. Available: {available}"
        lib_key, engine = resolved
        results = engine.search(query, top_k=top_k, language=lang)
        if not results:
            return f"No results in lib '{lib_key}'. Make sure it's indexed (use index_codebase with lib parameter)."
        code_lines = []
        for i, r in enumerate(results):
            summary = summarize_chunk(r['content'], r['language'])
            code_lines.append(
                f"[{i+1}] {r['source']}:{r['start_line']}-{r['end_line']} "
                f"({r['language']}, {r['score']:.0%}) {summary}"
            )
        return f"=== Lib: {lib_key} ===\n" + "\n".join(code_lines)

    if scope in ("main", "all"):
        proj_kb = [k for k in project_engine.search_knowledge(query, top_k=3) if k["score"] > 0.35]
        glob_kb = [k for k in global_engine.search_knowledge(query, top_k=3) if k["score"] > 0.35]
        output_parts.extend(_format_knowledge_results(proj_kb, "Project Knowledge"))
        output_parts.extend(_format_knowledge_results(glob_kb, "Global Knowledge"))

        results = project_engine.search(query, top_k=top_k, language=lang)
        if results:
            code_lines = []
            for i, r in enumerate(results):
                summary = summarize_chunk(r['content'], r['language'])
                code_lines.append(
                    f"[{i+1}] {r['source']}:{r['start_line']}-{r['end_line']} "
                    f"({r['language']}, {r['score']:.0%}) {summary}"
                )
            output_parts.append("=== Main ===\n" + "\n".join(code_lines))

    if scope in ("libs", "all") and lib_engines:
        for lib_key, engine in lib_engines.items():
            lib_results = engine.search(query, top_k=min(top_k, 5), language=lang)
            if lib_results:
                code_lines = []
                for i, r in enumerate(lib_results):
                    summary = summarize_chunk(r['content'], r['language'])
                    code_lines.append(
                        f"[{i+1}] {r['source']}:{r['start_line']}-{r['end_line']} "
                        f"({r['language']}, {r['score']:.0%}) {summary}"
                    )
                output_parts.append(f"=== Lib: {lib_key} ===\n" + "\n".join(code_lines))

    if not output_parts:
        return "No results found. Make sure the codebase has been indexed first (use index_codebase)."

    return "\n\n".join(output_parts)


@mcp.tool()
def get_index_status() -> str:
    status = project_engine.get_status()
    parts = []
    if not status["indexed"]:
        parts.append("Main: No index found. Run index_codebase to create one.")
    else:
        parts.append(
            f"Main index:\n"
            f"  Total files: {status['total_files']}\n"
            f"  Total chunks: {status['total_chunks']}"
        )

    for lib_key, engine in lib_engines.items():
        lib_status = engine.get_status()
        if lib_status["indexed"]:
            parts.append(f"Lib '{lib_key}': {lib_status['total_files']} files, {lib_status['total_chunks']} chunks")
        else:
            parts.append(f"Lib '{lib_key}': not indexed")

    return "\n".join(parts)


@mcp.tool()
def clear_index() -> str:
    project_engine.clear()
    return "Index cleared. Run index_codebase to rebuild."


@mcp.tool()
def list_libs() -> str:
    if not lib_engines:
        return "No external libraries configured. Add ragLibs to .mcp.json to configure."

    parts = [f"Configured libraries ({len(lib_engines)}):"]
    for lib_key, engine in lib_engines.items():
        lib_abs = os.path.normpath(os.path.join(PROJECT_ROOT, lib_key))
        exists = os.path.isdir(lib_abs)
        status = engine.get_status()
        if status["indexed"]:
            parts.append(f"  {lib_key}: {status['total_files']} files, {status['total_chunks']} chunks")
        elif exists:
            parts.append(f"  {lib_key}: not indexed (directory exists)")
        else:
            parts.append(f"  {lib_key}: directory not found ({lib_abs})")

    return "\n".join(parts)


@mcp.tool()
def add_knowledge(title: str, content: str, category: str = "general", tags: str = "", scope: str = "project") -> str:
    tag_list = [t.strip() for t in tags.split(",") if t.strip()] if tags else []
    results = []

    if scope in ("project", "both"):
        r = project_engine.add_knowledge(title=title, content=content, category=category, tags=tag_list)
        results.append(f"  [project] ID: {r['id']}")

    if scope in ("global", "both"):
        r = global_engine.add_knowledge(title=title, content=content, category=category, tags=tag_list)
        results.append(f"  [global]  ID: {r['id']}")

    return f"Knowledge added ({scope}):\n  Title: {title}\n  Category: {category}\n" + "\n".join(results)


@mcp.tool()
def search_knowledge(query: str, top_k: int = 5, category: str = "") -> str:
    top_k = max(1, min(20, top_k))
    cat = category if category else None

    proj_results = project_engine.search_knowledge(query, top_k=top_k, category=cat)
    glob_results = global_engine.search_knowledge(query, top_k=top_k, category=cat)

    if not proj_results and not glob_results:
        return "No knowledge entries found. Use add_knowledge to build the knowledge base."

    parts = []

    if proj_results:
        lines = []
        for i, r in enumerate(proj_results):
            tags_str = ", ".join(r["tags"]) if r["tags"] else "none"
            lines.append(
                f"[{i+1}] {r['title']} (id: {r['id']}, category: {r['category']}, tags: {tags_str}, score: {r['score']:.1%})\n"
                f"{r['content']}"
            )
        parts.append("=== Project Knowledge ===\n" + "\n\n---\n\n".join(lines))

    if glob_results:
        lines = []
        for i, r in enumerate(glob_results):
            tags_str = ", ".join(r["tags"]) if r["tags"] else "none"
            lines.append(
                f"[{i+1}] {r['title']} (id: {r['id']}, category: {r['category']}, tags: {tags_str}, score: {r['score']:.1%})\n"
                f"{r['content']}"
            )
        parts.append("=== Global Knowledge ===\n" + "\n\n---\n\n".join(lines))

    return "\n\n".join(parts)


@mcp.tool()
def remove_knowledge(entry_id: str, scope: str = "project") -> str:
    engine = global_engine if scope == "global" else project_engine
    ok = engine.remove_knowledge(entry_id)
    if ok:
        return f"Knowledge entry '{entry_id}' removed from {scope}."
    return f"Failed to remove entry '{entry_id}' from {scope}. It may not exist."


@mcp.tool()
def list_knowledge(category: str = "", scope: str = "") -> str:
    cat = category if category else None
    parts = []

    if scope in ("project", ""):
        entries = project_engine.list_knowledge(category=cat)
        if entries:
            status = project_engine.get_knowledge_status()
            header = f"Project KB: {status['total_entries']} entries"
            lines = []
            for e in entries:
                tags_str = ", ".join(e["tags"]) if e["tags"] else ""
                lines.append(f"  - [{e['id']}] {e['title']} ({e['category']}) {tags_str}")
            parts.append(header + "\n" + "\n".join(lines))

    if scope in ("global", ""):
        entries = global_engine.list_knowledge(category=cat)
        if entries:
            status = global_engine.get_knowledge_status()
            header = f"Global KB: {status['total_entries']} entries"
            lines = []
            for e in entries:
                tags_str = ", ".join(e["tags"]) if e["tags"] else ""
                lines.append(f"  - [{e['id']}] {e['title']} ({e['category']}) {tags_str}")
            parts.append(header + "\n" + "\n".join(lines))

    if not parts:
        return "No knowledge entries found."

    return "\n\n".join(parts)


@mcp.tool()
def compact_knowledge(scope: str = "project", threshold: float = 0.85) -> str:
    results = []
    if scope in ("project", "both"):
        r = project_engine.compact_knowledge(similarity_threshold=threshold)
        results.append(f"  [project] removed={r['removed']}, kept={r['kept']}")
    if scope in ("global", "both"):
        r = global_engine.compact_knowledge(similarity_threshold=threshold)
        results.append(f"  [global]  removed={r['removed']}, kept={r['kept']}")
    return "Compaction complete:\n" + "\n".join(results)


@mcp.tool()
def export_knowledge(scope: str = "project", category: str = "") -> str:
    cat = category if category else None
    parts = []

    if scope in ("project", "both"):
        md = project_engine.export_knowledge(category=cat)
        if md:
            parts.append(f"# Project Knowledge\n\n{md}")

    if scope in ("global", "both"):
        md = global_engine.export_knowledge(category=cat)
        if md:
            parts.append(f"# Global Knowledge\n\n{md}")

    if not parts:
        return "No knowledge entries to export."

    return "\n\n---\n\n".join(parts)


@mcp.tool()
def get_dependency_graph(file_path: str) -> str:
    abs_path = file_path if os.path.isabs(file_path) else os.path.join(PROJECT_ROOT, file_path)
    result = _get_dep_graph(abs_path, PROJECT_ROOT)

    if "error" in result:
        return f"Error: {result['error']}"

    parts = [f"File: {result['file']}"]

    if result["imports"]:
        lines = []
        for imp in result["imports"]:
            resolved = imp["resolved"] or "(unresolved)"
            lines.append(f"  {imp['raw']} -> {resolved}")
        parts.append(f"Imports ({len(result['imports'])}):\n" + "\n".join(lines))
    else:
        parts.append("Imports: none")

    if result["imported_by"]:
        lines = [f"  {f}" for f in result["imported_by"]]
        parts.append(f"Imported by ({len(result['imported_by'])}):\n" + "\n".join(lines))
    else:
        parts.append("Imported by: none")

    return "\n\n".join(parts)


@mcp.tool()
def find_similar_code(code_snippet: str, top_k: int = 10) -> str:
    top_k = max(1, min(30, top_k))
    results = _find_similar(code_snippet, project_engine, top_k=top_k)

    if not results:
        return "No similar code found. Make sure the codebase is indexed."

    lines = []
    for i, r in enumerate(results):
        summary = summarize_chunk(r['content'], r['language'])
        lines.append(
            f"[{i+1}] {r['source']}:{r['start_line']}-{r['end_line']} "
            f"({r['language']}, {r['score']:.0%}) {summary}"
        )
    return "\n".join(lines)


@mcp.tool()
def index_symbols() -> str:
    symbols = collect_all_symbols(PROJECT_ROOT)
    result = project_engine.index_symbols(symbols)
    by_kind: dict[str, int] = {}
    for s in symbols:
        by_kind[s["kind"]] = by_kind.get(s["kind"], 0) + 1
    kind_str = ", ".join(f"{v} {k}s" for k, v in sorted(by_kind.items(), key=lambda x: -x[1]))
    return f"Symbol index built: {result['indexed']} symbols ({kind_str})"


@mcp.tool()
def lookup_symbol(name: str, kind: str = "", language: str = "") -> str:
    results = project_engine.lookup_symbol(name, kind=kind, language=language)
    if not results:
        status = project_engine.get_symbol_status()
        if not status["indexed"]:
            return "No symbol index found. Run index_symbols first."
        return f"No symbols matching '{name}' found."

    lines = []
    for r in results:
        sig = f" {r['signature']}" if r['signature'] else ""
        lines.append(f"  [{r['kind']}] {r['name']}{sig}  ({r['file']}:{r['line']})")
    return f"Found {len(results)} symbol(s):\n" + "\n".join(lines)


@mcp.tool()
def search_symbols(query: str, top_k: int = 20, kind: str = "") -> str:
    top_k = max(1, min(50, top_k))
    results = project_engine.search_symbols(query, top_k=top_k, kind=kind)
    if not results:
        status = project_engine.get_symbol_status()
        if not status["indexed"]:
            return "No symbol index found. Run index_symbols first."
        return "No matching symbols found."

    lines = []
    for i, r in enumerate(results):
        sig = f" {r['signature']}" if r['signature'] else ""
        lines.append(
            f"[{i+1}] [{r['kind']}] {r['name']}{sig}\n"
            f"     {r['file']}:{r['line']} ({r['language']}, score: {r['score']:.1%})"
        )
    return "\n".join(lines)


@mcp.tool()
def get_file_summary(file_path: str) -> str:
    abs_path = file_path if os.path.isabs(file_path) else os.path.join(PROJECT_ROOT, file_path)
    result = _file_summary(abs_path)

    if "error" in result:
        return f"Error: {result['error']}"

    parts = [f"File: {result['file']} ({result['lines']} lines)"]

    if result["by_kind"]:
        kind_str = ", ".join(f"{v} {k}(s)" for k, v in sorted(result["by_kind"].items(), key=lambda x: -x[1]))
        parts.append(f"Symbols: {kind_str}")

    if result["symbols"]:
        by_kind: dict[str, list] = {}
        for s in result["symbols"]:
            by_kind.setdefault(s["kind"], []).append(s)

        for kind, syms in sorted(by_kind.items()):
            lines = []
            for s in syms[:30]:
                sig = f" {s['signature']}" if s['signature'] else ""
                lines.append(f"    L{s['line']}: {s['name']}{sig}")
            overflow = f"\n    ... and {len(syms) - 30} more" if len(syms) > 30 else ""
            parts.append(f"  [{kind}]\n" + "\n".join(lines) + overflow)

    return "\n".join(parts)


@mcp.tool()
def get_module_map(directory: str = "", max_depth: int = 3) -> str:
    target = os.path.join(PROJECT_ROOT, directory) if directory else PROJECT_ROOT
    if not os.path.isdir(target):
        return f"Error: directory not found: {target}"

    tree = _module_map(target, max_depth=max_depth)
    formatted = _format_module_map(tree)
    return formatted if formatted else "Empty directory or no code files found."


@mcp.tool()
def find_callers(symbol_name: str, language: str = "") -> str:
    results = _find_callers(symbol_name, PROJECT_ROOT, lang_filter=language)
    if not results:
        return f"No callers found for '{symbol_name}'."

    lines = [f"  {r['file']}:{r['line']} — {r['text']}" for r in results[:50]]
    overflow = f"\n  ... and {len(results) - 50} more" if len(results) > 50 else ""
    return f"Found {len(results)} call site(s) for '{symbol_name}':\n" + "\n".join(lines) + overflow


@mcp.tool()
def type_hierarchy(type_name: str = "") -> str:
    result = _get_type_hierarchy(PROJECT_ROOT)
    types = result["types"]

    if not types:
        return "No type hierarchy found. Make sure project has classes/structs/traits."

    if type_name:
        if type_name not in types:
            matches = [n for n in types if type_name.lower() in n.lower()]
            if not matches:
                return f"Type '{type_name}' not found."
            parts = [f"Partial matches for '{type_name}':"]
            for m in matches[:20]:
                t = types[m]
                parts.append(f"  [{t['kind']}] {m} ({t['file']}:{t['line']})")
            return "\n".join(parts)

        t = types[type_name]
        parts = [f"[{t['kind']}] {type_name} ({t['file']}:{t['line']})"]
        if t["extends"]:
            parts.append(f"  extends: {', '.join(t['extends'])}")
        if t["implements"]:
            parts.append(f"  implements: {', '.join(t['implements'])}")
        if t["extended_by"]:
            parts.append(f"  extended by: {', '.join(t['extended_by'])}")
        if t["implemented_by"]:
            parts.append(f"  implemented by: {', '.join(t['implemented_by'])}")
        return "\n".join(parts)

    roots = [n for n, t in types.items() if not t["extends"] and (t["extended_by"] or t["implemented_by"])]
    parts = [f"Type hierarchy: {len(types)} types, {len(result['edges'])} edges"]

    for r in sorted(roots)[:50]:
        t = types[r]
        parts.append(f"\n[{t['kind']}] {r}")
        for child in t.get("extended_by", []):
            parts.append(f"  <- {child} (extends)")
        for child in t.get("implemented_by", []):
            parts.append(f"  <- {child} (implements)")

    return "\n".join(parts)


@mcp.tool()
def cross_language_trace(symbol_name: str) -> str:
    result = _trace_cross_lang(symbol_name, PROJECT_ROOT)

    parts = [f"Cross-language trace for '{symbol_name}':"]

    if result["rust_definition"]:
        rd = result["rust_definition"]
        wasm_tag = " [wasm_bindgen]" if rd["is_wasm_export"] else ""
        parts.append(f"\nRust definition: {rd['file']}:{rd['line']}{wasm_tag}")
    else:
        parts.append("\nRust definition: not found")

    if result["wasm_bridge"]:
        parts.append(f"\nWASM bridge ({len(result['wasm_bridge'])}):")
        for br in result["wasm_bridge"][:10]:
            parts.append(f"  {br['file']}:{br['line']} — {br['text'][:100]}")

    if result["ts_callers"]:
        parts.append(f"\nTS callers ({len(result['ts_callers'])}):")
        for tc in result["ts_callers"][:20]:
            parts.append(f"  {tc['file']}:{tc['line']} — {tc['text'][:100]}")

    if result["chain"]:
        parts.append(f"\nCall chain:\n  " + "\n  -> ".join(result["chain"]))

    return "\n".join(parts)




@mcp.tool()
def bulk_rename_preview(old_name: str, new_name: str, language: str = "") -> str:
    results = _preview_rename(old_name, new_name, PROJECT_ROOT, language=language)
    if not results:
        return f"No occurrences of '{old_name}' found."

    would_rename = [r for r in results if r["would_rename"]]
    would_skip = [r for r in results if not r["would_rename"]]

    by_cat: dict[str, list] = {}
    for r in would_rename:
        by_cat.setdefault(r["category"], []).append(r)

    parts = [f"Rename '{old_name}' -> '{new_name}': {len(would_rename)} locations to rename, {len(would_skip)} to skip"]

    for cat, entries in sorted(by_cat.items()):
        parts.append(f"\n[{cat}] ({len(entries)})")
        for e in entries[:20]:
            parts.append(f"  {e['file']}:{e['line']}:{e['column']} — {e['text'][:100]}")
        if len(entries) > 20:
            parts.append(f"  ... and {len(entries) - 20} more")

    if would_skip:
        parts.append(f"\nSkipped ({len(would_skip)}, in strings/comments):")
        for e in would_skip[:10]:
            parts.append(f"  {e['file']}:{e['line']} [{e['category']}] — {e['text'][:80]}")

    return "\n".join(parts)


@mcp.tool()
def get_function_body(function_name: str, file_path: str = "", language: str = "") -> str:
    from chunker import get_function_body as _get_body

    if file_path:
        abs_path = file_path if os.path.isabs(file_path) else os.path.join(PROJECT_ROOT, file_path)
        if not os.path.isfile(abs_path):
            return f"File not found: {abs_path}"
        try:
            content = open(abs_path, encoding="utf-8", errors="ignore").read()
        except Exception as e:
            return f"Error reading file: {e}"
        lang = language if language else ext_to_lang(os.path.splitext(abs_path)[1])
        result = _get_body(content, lang, function_name)
        if result:
            return f"{abs_path}:{result['start_line']}-{result['end_line']} [{result['kind']}]\n{result['content']}"
        return f"Function '{function_name}' not found in {abs_path}"

    results = project_engine.lookup_symbol(function_name, kind="", language=language)
    if not results:
        return f"Symbol '{function_name}' not found. Try index_symbols first."

    parts = []
    seen = set()
    for sym in results[:5]:
        if sym["file"] in seen:
            continue
        seen.add(sym["file"])
        try:
            content = open(sym["file"], encoding="utf-8", errors="ignore").read()
        except Exception:
            continue
        lang = language if language else ext_to_lang(os.path.splitext(sym["file"])[1])
        result = _get_body(content, lang, function_name)
        if result:
            parts.append(f"{sym['file']}:{result['start_line']}-{result['end_line']} [{result['kind']}]\n{result['content']}")

    if not parts:
        locs = [f"  {s['file']}:{s['line']} [{s['kind']}]" for s in results[:5]]
        return f"Found symbol but couldn't extract body:\n" + "\n".join(locs)

    return "\n\n---\n\n".join(parts)


if __name__ == "__main__":
    mcp.run(transport="stdio")
