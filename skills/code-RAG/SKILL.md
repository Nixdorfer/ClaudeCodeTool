---
name: code-RAG
description: Local code RAG KB. 34 MCP tools for semantic code search, knowledge management, symbol lookup, code analysis. Load this skill before using any mcp__code-RAG__ tool.
allowed-tools: mcp__code-RAG__*
---

## Workflow (MUST follow)

1. During task: after each code change call `index_codebase`. Append what changed and why to `PROJECT_ROOT/.claude/plans/*TASK_DESC*.md`. DO NOT call `add_knowledge` yet.
2. When user confirms task complete: summarize `*TASK_DESC*.md` into one `add_knowledge` call (English, minimize tokens). Bugfix→scope=both. Others→scope=project. Then delete `*TASK_DESC*.md`.

## Tool index (load subfile for usage)

[Search & index](search.md) — index_codebase, search_code, get_index_status, clear_index, index_symbols, find_similar_code
[Knowledge](knowledge.md) — add_knowledge, search_knowledge, remove_knowledge, list_knowledge, compact_knowledge, export_knowledge
[Symbols](symbols.md) — lookup_symbol, search_symbols, find_callers, get_file_summary, get_module_map, get_function_body
[Trace](code-trace.md) — get_dependency_graph, type_hierarchy, cross_language_trace, bulk_rename_preview