---
name: code-RAG
description: Local code RAG KB. 34 MCP tools for semantic code search, knowledge management, symbol lookup, code analysis. Load this skill before using any mcp__code-RAG__ tool.
---

After each task, silently: 1) index_codebase 2) add_knowledge.
Knowledge: English, minimal tokens. bugfix→wait confirm then scope=project+global. Others→immediate scope=project.

## Tool index (load subfile for usage)

[Search & index](search.md) — index_codebase, search_code, get_index_status, clear_index, index_symbols, find_similar_code
[Knowledge](knowledge.md) — add_knowledge, search_knowledge, remove_knowledge, list_knowledge, compact_knowledge, export_knowledge
[Symbols](symbols.md) — lookup_symbol, search_symbols, find_callers, get_file_summary, get_module_map, get_function_body
[Context](context.md) — get_project_summary, save_context, load_context
[Git](git-analysis.md) — get_recent_changes, diff_analysis, config_diff, changelog
[Quality](code-quality.md) — find_dead_code, complexity_hotspots, detect_antipatterns, find_orphans, scan_annotations
[Trace](code-trace.md) — get_dependency_graph, type_hierarchy, cross_language_trace, bulk_rename_preview
