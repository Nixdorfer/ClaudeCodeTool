import os
import sys
import logging

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
from analysis import (
    get_dependency_graph as _get_dep_graph,
    find_orphan_files as _find_orphans,
    scan_annotations as _scan_annotations,
    find_similar_code as _find_similar,
    get_recent_changes as _get_recent,
    get_project_summary as _get_summary,
    analyze_diff as _analyze_diff,
    trace_cross_language as _trace_cross_lang,
    diff_configs as _diff_configs,
    generate_changelog as _gen_changelog,
    save_context_snapshot as _save_snapshot,
    load_context_snapshot as _load_snapshot,
)
from symbols import (
    collect_all_symbols,
    find_callers as _find_callers,
    get_type_hierarchy as _get_type_hierarchy,
    find_dead_code as _find_dead_code,
    preview_rename as _preview_rename,
)
from structure import (
    file_summary as _file_summary,
    module_map as _module_map,
    format_module_map as _format_module_map,
)
from complexity import find_hotspots as _find_hotspots
from patterns import detect_patterns as _detect_patterns

PROJECT_ROOT = os.environ.get("PROJECT_ROOT") or os.getcwd()
PROJECT_DB = os.environ.get("RAG_DB_PATH") or os.path.join(PROJECT_ROOT, ".claude", "mcp", "code-RAG")
GLOBAL_DB = os.path.join(os.path.expanduser("~"), ".claude", "mcp", "code-RAG", "global_kb")
MODEL_NAME = os.environ.get("RAG_MODEL", "all-MiniLM-L6-v2")

os.makedirs(PROJECT_DB, exist_ok=True)
os.makedirs(GLOBAL_DB, exist_ok=True)

shared_model = SentenceTransformer(MODEL_NAME)
project_engine = RAGEngine(db_path=PROJECT_DB, model=shared_model)
global_engine = RAGEngine(db_path=GLOBAL_DB, model=shared_model)

mcp = FastMCP(
    "code-RAG",
    instructions=(
        "Prefer search_code over Glob/Grep for open-ended code searches.\n"
        "After completing each task, silently: 1) index_codebase 2) add_knowledge.\n"
        "Knowledge: English, minimize tokens. Categories: bugfix/decision/pattern/operation/architecture.\n"
        "Bugfix: wait for user confirmation, then add_knowledge scope=project + scope=global.\n"
        "Others: write immediately, scope=project."
    ),
)

logger.info(f"code-RAG started | project={PROJECT_ROOT} | project_db={PROJECT_DB} | global_db={GLOBAL_DB}")


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


@mcp.tool()
def index_codebase(directory: str = "") -> str:
    target = directory if directory else PROJECT_ROOT
    if not os.path.isdir(target):
        return f"Error: directory not found: {target}"

    logger.info(f"Indexing: {target}")
    result = project_engine.index_directory(target)

    symbols = collect_all_symbols(target)
    sym_result = project_engine.index_symbols(symbols)

    return (
        f"Indexing complete:\n"
        f"  Total files scanned: {result['total_files']}\n"
        f"  Files indexed (new/changed): {result['indexed']}\n"
        f"  Files skipped (unchanged): {result['skipped_unchanged']}\n"
        f"  Chunks created: {result['chunks_created']}\n"
        f"  Symbols indexed: {sym_result['indexed']}"
    )


@mcp.tool()
def search_code(query: str, top_k: int = 10, language: str = "") -> str:
    top_k = max(1, min(30, top_k))
    lang = language if language else None
    results = project_engine.search(query, top_k=top_k, language=lang)

    output_parts = []

    proj_kb = [k for k in project_engine.search_knowledge(query, top_k=3) if k["score"] > 0.35]
    glob_kb = [k for k in global_engine.search_knowledge(query, top_k=3) if k["score"] > 0.35]
    output_parts.extend(_format_knowledge_results(proj_kb, "Project Knowledge"))
    output_parts.extend(_format_knowledge_results(glob_kb, "Global Knowledge"))

    if not results:
        if output_parts:
            output_parts.append("(No code results found)")
            return "\n\n".join(output_parts)
        return "No results found. Make sure the codebase has been indexed first (use index_codebase)."

    code_lines = []
    for i, r in enumerate(results):
        summary = summarize_chunk(r['content'], r['language'])
        code_lines.append(
            f"[{i+1}] {r['source']}:{r['start_line']}-{r['end_line']} "
            f"({r['language']}, {r['score']:.0%}) {summary}"
        )
    output_parts.append("\n".join(code_lines))

    return "\n\n".join(output_parts)


@mcp.tool()
def get_index_status() -> str:
    status = project_engine.get_status()
    if not status["indexed"]:
        return "No index found. Run index_codebase to create one."
    return (
        f"Index status:\n"
        f"  Total files: {status['total_files']}\n"
        f"  Total chunks: {status['total_chunks']}"
    )


@mcp.tool()
def clear_index() -> str:
    project_engine.clear()
    return "Index cleared. Run index_codebase to rebuild."


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
def get_project_summary() -> str:
    summary = _get_summary(PROJECT_ROOT, project_engine)

    parts = [f"Project: {summary['project_root']}"]

    idx = summary["index"]
    sym_status = project_engine.get_symbol_status()
    sym_str = f", {sym_status['total_symbols']} symbols" if sym_status["indexed"] else ""
    parts.append(f"Index: {idx['total_files']} files, {idx['total_chunks']} chunks{sym_str}")

    kb = summary["knowledge"]
    if kb["has_knowledge"]:
        parts.append(f"Knowledge: {kb['total_entries']} entries ({', '.join(kb['categories'])})")

    if summary["language_distribution"]:
        lang_lines = [f"  {lang}: {count} chunks" for lang, count in
                      sorted(summary["language_distribution"].items(), key=lambda x: -x[1])[:8]]
        parts.append("Languages:\n" + "\n".join(lang_lines))

    if summary["recent_knowledge"]:
        kb_lines = [f"  [{e['category']}] {e['title']}" for e in summary["recent_knowledge"]]
        parts.append("Recent knowledge:\n" + "\n".join(kb_lines))

    git = summary["recent_git"]
    if "error" not in git:
        if git.get("hot_files"):
            hot_lines = [f"  {f['file']} ({f['changes']}x)" for f in git["hot_files"][:10]]
            parts.append("Hot files (most changed):\n" + "\n".join(hot_lines))
        if git.get("uncommitted"):
            parts.append(f"Uncommitted changes:\n  {git['uncommitted'][:500]}")

    return "\n\n".join(parts)


@mcp.tool()
def get_recent_changes(count: int = 20) -> str:
    result = _get_recent(PROJECT_ROOT, count=count)
    if "error" in result:
        return f"Error: {result['error']}"

    parts = []
    if result.get("log"):
        parts.append(f"=== Recent {count} Commits ===\n{result['log']}")

    if result.get("uncommitted"):
        parts.append(f"=== Uncommitted Changes ===\n{result['uncommitted']}")

    if result.get("hot_files"):
        lines = [f"  {f['file']} ({f['changes']}x)" for f in result["hot_files"]]
        parts.append("=== Hot Files ===\n" + "\n".join(lines))

    return "\n\n".join(parts) if parts else "No git history found."


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
def find_orphans() -> str:
    result = _find_orphans(PROJECT_ROOT)

    if not result["orphans"]:
        return f"No orphan files found among {result['total_files']} files."

    lines = [f for f in result["orphans"]]
    header = f"Found {result['orphan_count']} potentially orphaned files (out of {result['total_files']}):"
    return header + "\n" + "\n".join(f"  {f}" for f in lines[:50])


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
def scan_annotations(annotation_type: str = "") -> str:
    results = _scan_annotations(PROJECT_ROOT, annotation_type=annotation_type)

    if not results:
        filter_msg = f" of type '{annotation_type}'" if annotation_type else ""
        return f"No annotations{filter_msg} found."

    by_type: dict[str, list] = {}
    for r in results:
        by_type.setdefault(r["type"], []).append(r)

    parts = [f"Found {len(results)} annotations:"]
    for atype, entries in sorted(by_type.items()):
        lines = [f"  {e['file']}:{e['line']} — {e['text']}" for e in entries[:20]]
        overflow = f"\n  ... and {len(entries) - 20} more" if len(entries) > 20 else ""
        parts.append(f"\n[{atype}] ({len(entries)})\n" + "\n".join(lines) + overflow)

    return "\n".join(parts)


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
def diff_analysis(ref: str = "") -> str:
    result = _analyze_diff(PROJECT_ROOT, ref=ref)
    if "error" in result:
        return f"Error: {result['error']}"

    parts = [f"Diff against: {result['ref']}", f"Files changed: {result['files_changed']} (+{result['insertions']} -{result['deletions']})"]

    for cf in result["changed_files"][:30]:
        sym_str = ""
        if cf["affected_symbols"]:
            sym_names = [f"{s['name']}({s['kind']})" for s in cf["affected_symbols"][:5]]
            sym_str = f"  affected: {', '.join(sym_names)}"
        parts.append(f"  {cf['file']} (+{cf['insertions']} -{cf['deletions']}){sym_str}")

    if result["impact"]:
        parts.append(f"\nImpacted files ({len(result['impact'])}):")
        for f in result["impact"][:20]:
            parts.append(f"  {f}")

    return "\n".join(parts)


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
def find_dead_code(language: str = "") -> str:
    results = _find_dead_code(PROJECT_ROOT, language=language)
    if not results:
        return "No dead code found (or project is small enough that all functions are referenced)."

    by_lang: dict[str, list] = {}
    for r in results:
        by_lang.setdefault(r["language"], []).append(r)

    parts = [f"Found {len(results)} potentially dead functions:"]
    for lang, entries in sorted(by_lang.items()):
        parts.append(f"\n[{lang}] ({len(entries)})")
        for e in entries[:30]:
            parts.append(f"  {e['file']}:{e['line']} [{e['kind']}] {e['name']}")
        if len(entries) > 30:
            parts.append(f"  ... and {len(entries) - 30} more")

    return "\n".join(parts)


@mcp.tool()
def complexity_hotspots(directory: str = "", top_n: int = 30) -> str:
    target = os.path.join(PROJECT_ROOT, directory) if directory else PROJECT_ROOT
    results = _find_hotspots(target, top_n=top_n)

    if not results:
        return "No functions found to analyze."

    parts = [f"Top {len(results)} most complex functions:"]
    for i, r in enumerate(results):
        parts.append(
            f"[{i+1}] {r['name']} (complexity={r['complexity']}, nesting={r['nesting_depth']}, lines={r['lines']})\n"
            f"     {r['file']}:{r['line']} ({r.get('language', '')})"
        )

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
def config_diff() -> str:
    result = _diff_configs(PROJECT_ROOT)

    changed = [c for c in result["configs"] if c["has_changes"]]
    if not changed:
        return f"No config changes detected ({len(result['configs'])} config files checked)."

    parts = [f"{len(changed)} config file(s) changed:"]
    for c in changed:
        parts.append(f"\n{c['file']} ({c['diff_summary']})")
        if c["added_deps"]:
            parts.append(f"  + deps: {', '.join(c['added_deps'])}")
        if c["removed_deps"]:
            parts.append(f"  - deps: {', '.join(c['removed_deps'])}")
        if c["changed_settings"]:
            parts.append(f"  settings: {', '.join(c['changed_settings'])}")

    return "\n".join(parts)


@mcp.tool()
def detect_antipatterns(checks: str = "", directory: str = "") -> str:
    target = os.path.join(PROJECT_ROOT, directory) if directory else PROJECT_ROOT
    check_list = [c.strip() for c in checks.split(",") if c.strip()] if checks else None
    results = _detect_patterns(target, checks=check_list)

    if not results:
        return "No anti-patterns detected."

    by_check: dict[str, list] = {}
    for r in results:
        by_check.setdefault(r["check"], []).append(r)

    parts = [f"Found {len(results)} findings:"]
    for check, entries in sorted(by_check.items()):
        sev_counts = {}
        for e in entries:
            sev_counts[e["severity"]] = sev_counts.get(e["severity"], 0) + 1
        sev_str = ", ".join(f"{v} {k}" for k, v in sorted(sev_counts.items()))
        parts.append(f"\n[{check}] ({len(entries)}: {sev_str})")
        for e in entries[:15]:
            parts.append(f"  [{e['severity']}] {e['file']}:{e['line']} — {e['message']}")
        if len(entries) > 15:
            parts.append(f"  ... and {len(entries) - 15} more")

    return "\n".join(parts)


@mcp.tool()
def changelog(since: str = "", count: int = 50) -> str:
    return _gen_changelog(PROJECT_ROOT, since=since, count=count)


@mcp.tool()
def save_context(active_files: str = "", current_task: str = "", notes: str = "") -> str:
    data: dict = {}
    if active_files:
        data["active_files"] = [f.strip() for f in active_files.split(",") if f.strip()]
    if current_task:
        data["current_task"] = current_task
    if notes:
        data["notes"] = notes

    path = _save_snapshot(PROJECT_ROOT, data)
    return f"Context saved to {path}"


@mcp.tool()
def load_context() -> str:
    data = _load_snapshot(PROJECT_ROOT)
    if "error" in data:
        return f"No saved context found."

    parts = []
    if data.get("_branch"):
        parts.append(f"Branch: {data['_branch']}")
    if data.get("_timestamp"):
        import time
        ts = time.strftime("%Y-%m-%d %H:%M", time.localtime(data["_timestamp"]))
        parts.append(f"Saved: {ts}")
    if data.get("current_task"):
        parts.append(f"Task: {data['current_task']}")
    if data.get("active_files"):
        parts.append(f"Active files:\n" + "\n".join(f"  {f}" for f in data["active_files"]))
    if data.get("notes"):
        parts.append(f"Notes: {data['notes']}")

    return "\n".join(parts) if parts else "Context loaded but empty."


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
        from rag_engine import _ext_to_lang
        lang = language if language else _ext_to_lang(os.path.splitext(abs_path)[1])
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
        from rag_engine import _ext_to_lang
        lang = language if language else _ext_to_lang(os.path.splitext(sym["file"])[1])
        result = _get_body(content, lang, function_name)
        if result:
            parts.append(f"{sym['file']}:{result['start_line']}-{result['end_line']} [{result['kind']}]\n{result['content']}")

    if not parts:
        locs = [f"  {s['file']}:{s['line']} [{s['kind']}]" for s in results[:5]]
        return f"Found symbol but couldn't extract body:\n" + "\n".join(locs)

    return "\n\n---\n\n".join(parts)


if __name__ == "__main__":
    mcp.run(transport="stdio")
