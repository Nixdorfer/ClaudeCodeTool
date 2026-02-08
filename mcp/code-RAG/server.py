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

from mcp.server.fastmcp import FastMCP
from rag_engine import RAGEngine

PROJECT_ROOT = os.environ.get("PROJECT_ROOT") or os.getcwd()
DB_PATH = os.environ.get("RAG_DB_PATH") or os.path.join(PROJECT_ROOT, ".claude", "mcp", "code-RAG")
MODEL_NAME = os.environ.get("RAG_MODEL", "all-MiniLM-L6-v2")

os.makedirs(DB_PATH, exist_ok=True)

mcp = FastMCP(
    "code-RAG",
    instructions=(
        "You have a project-local code RAG (Retrieval-Augmented Generation) knowledge base.\n"
        "Prefer search_code over Glob/Grep for open-ended code searches.\n"
        "\n"
        "After completing each task, you MUST silently (without reporting to user):\n"
        "1. Call index_codebase to update the code index\n"
        "2. Call add_knowledge to log: what was done, which files changed, key decisions\n"
        "\n"
        "Knowledge entry rules:\n"
        "- Use English, minimize tokens\n"
        "- Categories: bugfix / decision / pattern / operation / architecture\n"
        "- For bugfix: do NOT write immediately. Wait for user confirmation that fix works,\n"
        "  then record: symptoms, root cause, fix approach (category=bugfix)\n"
        "- All other categories: write immediately after task completion\n"
    ),
)
engine = RAGEngine(db_path=DB_PATH, model_name=MODEL_NAME)

logger.info(f"code-RAG started | project={PROJECT_ROOT} | db={DB_PATH} | model={MODEL_NAME}")


@mcp.tool()
def index_codebase(directory: str = "") -> str:
    """Index source code files in a directory for semantic search.
    If directory is empty, indexes the project root.
    Supports incremental indexing - only changed files are re-indexed.

    Args:
        directory: Directory path to index. Empty string = project root.
    """
    target = directory if directory else PROJECT_ROOT
    if not os.path.isdir(target):
        return f"Error: directory not found: {target}"

    logger.info(f"Indexing: {target}")
    result = engine.index_directory(target)
    return (
        f"Indexing complete:\n"
        f"  Total files scanned: {result['total_files']}\n"
        f"  Files indexed (new/changed): {result['indexed']}\n"
        f"  Files skipped (unchanged): {result['skipped_unchanged']}\n"
        f"  Chunks created: {result['chunks_created']}"
    )


@mcp.tool()
def search_code(query: str, top_k: int = 10, language: str = "") -> str:
    """Search the indexed codebase using semantic similarity.
    Returns the most relevant code snippets for the given query.
    Automatically includes relevant knowledge base entries (bugfixes, patterns, decisions).

    Args:
        query: Natural language search query (e.g. "terrain chunk mesh generation")
        top_k: Number of results to return (1-30)
        language: Optional language filter (e.g. "rust", "typescript")
    """
    top_k = max(1, min(30, top_k))
    lang = language if language else None
    results = engine.search(query, top_k=top_k, language=lang)

    output_parts = []

    knowledge_results = engine.search_knowledge(query, top_k=3)
    relevant = [k for k in knowledge_results if k["score"] > 0.35]
    if relevant:
        kb_lines = []
        for k in relevant:
            tags_str = ", ".join(k["tags"]) if k["tags"] else ""
            kb_lines.append(
                f"  [{k['category']}] {k['title']} (score: {k['score']:.1%}){' | ' + tags_str if tags_str else ''}\n"
                f"  {k['content']}"
            )
        output_parts.append("=== Knowledge Base Matches ===\n" + "\n\n".join(kb_lines))

    if not results:
        if output_parts:
            output_parts.append("(No code results found)")
            return "\n\n".join(output_parts)
        return "No results found. Make sure the codebase has been indexed first (use index_codebase)."

    code_lines = []
    for i, r in enumerate(results):
        code_lines.append(
            f"[{i+1}] {r['source']}:{r['start_line']}-{r['end_line']} "
            f"({r['language']}, score: {r['score']:.1%})\n"
            f"{r['content']}"
        )
    output_parts.append("\n\n---\n\n".join(code_lines))

    return "\n\n".join(output_parts)


@mcp.tool()
def get_index_status() -> str:
    """Check the current status of the code index.
    Returns the number of indexed files and chunks.
    """
    status = engine.get_status()
    if not status["indexed"]:
        return "No index found. Run index_codebase to create one."
    return (
        f"Index status:\n"
        f"  Total files: {status['total_files']}\n"
        f"  Total chunks: {status['total_chunks']}"
    )


@mcp.tool()
def clear_index() -> str:
    """Clear the entire code index. Use this to force a full re-index."""
    engine.clear()
    return "Index cleared. Run index_codebase to rebuild."


@mcp.tool()
def add_knowledge(title: str, content: str, category: str = "general", tags: str = "") -> str:
    """Add a knowledge entry to the knowledge base for later retrieval.
    Use this to record decisions, patterns, bug fixes, operation logs, or any reusable information.

    Args:
        title: Short descriptive title for the knowledge entry.
        content: The full knowledge content (explanation, steps, context, etc.)
        category: Category for organization (e.g. "bugfix", "decision", "pattern", "operation", "architecture")
        tags: Comma-separated tags for filtering (e.g. "rust,wasm,terrain")
    """
    tag_list = [t.strip() for t in tags.split(",") if t.strip()] if tags else []
    result = engine.add_knowledge(title=title, content=content, category=category, tags=tag_list)
    return f"Knowledge added:\n  ID: {result['id']}\n  Title: {result['title']}\n  Category: {result['category']}"


@mcp.tool()
def search_knowledge(query: str, top_k: int = 5, category: str = "") -> str:
    """Search the knowledge base using semantic similarity.
    Returns the most relevant knowledge entries for the given query.

    Args:
        query: Natural language search query (e.g. "how to fix terrain LOD flickering")
        top_k: Number of results to return (1-20)
        category: Optional category filter (e.g. "bugfix", "decision", "pattern")
    """
    top_k = max(1, min(20, top_k))
    cat = category if category else None
    results = engine.search_knowledge(query, top_k=top_k, category=cat)

    if not results:
        return "No knowledge entries found. Use add_knowledge to build the knowledge base."

    parts = []
    for i, r in enumerate(results):
        tags_str = ", ".join(r["tags"]) if r["tags"] else "none"
        parts.append(
            f"[{i+1}] {r['title']} (id: {r['id']}, category: {r['category']}, tags: {tags_str}, score: {r['score']:.1%})\n"
            f"{r['content']}"
        )
    return "\n\n---\n\n".join(parts)


@mcp.tool()
def remove_knowledge(entry_id: str) -> str:
    """Remove a knowledge entry by its ID.

    Args:
        entry_id: The ID of the knowledge entry to remove.
    """
    ok = engine.remove_knowledge(entry_id)
    if ok:
        return f"Knowledge entry '{entry_id}' removed."
    return f"Failed to remove entry '{entry_id}'. It may not exist."


@mcp.tool()
def list_knowledge(category: str = "") -> str:
    """List all knowledge entries, optionally filtered by category.

    Args:
        category: Optional category filter. Empty string = all categories.
    """
    cat = category if category else None
    entries = engine.list_knowledge(category=cat)

    if not entries:
        return "No knowledge entries found."

    status = engine.get_knowledge_status()
    header = f"Knowledge base: {status['total_entries']} entries, categories: {', '.join(status['categories'])}\n\n"

    lines = []
    for e in entries:
        tags_str = ", ".join(e["tags"]) if e["tags"] else ""
        lines.append(f"- [{e['id']}] {e['title']} ({e['category']}) {tags_str}")
    return header + "\n".join(lines)


if __name__ == "__main__":
    mcp.run(transport="stdio")
