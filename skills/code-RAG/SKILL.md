---
name: code-RAG
description: Local code RAG KB. 23 MCP tools for semantic code search, knowledge management, symbol lookup, etc. Load this skill before using any mcp__code-RAG__ tool or doing bug fix.
allowed-tools: mcp__code-RAG__*
---

# Tool index

当你尝试搜索代码或者获取总览时 请先查看这些工具
[Search & index](search.md) — index_codebase, search_code, get_index_status, clear_index, list_libs, index_symbols, find_similar_code

当你尝试总结经验时 请先查看这些工具
[Knowledge](knowledge.md) — add_knowledge, search_knowledge, remove_knowledge, list_knowledge, compact_knowledge, export_knowledge

当你尝试搜索符号时 请先查看这些工具
[Symbols](symbols.md) — lookup_symbol, search_symbols, find_callers, get_file_summary, get_module_map, get_function_body

当你尝试探索代码结构或者关系时 请先查看这些工具
[Trace](code-trace.md) — get_dependency_graph, type_hierarchy, cross_language_trace, bulk_rename_preview