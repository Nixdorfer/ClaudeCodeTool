# Knowledge Management

### add_knowledge(title, content, category="general", tags="", scope="project")
- category: bugfix/decision/pattern/operation/architecture
- tags: comma-separated
- scope: "project"/"global"/"both"

### search_knowledge(query, top_k=5, category="")
Semantic search across project+global KB.

### remove_knowledge(entry_id, scope="project")
Delete by ID.

### list_knowledge(category="", scope="")
List all entries. Filter by category/scope.

### compact_knowledge(scope="project", threshold=0.85)
Deduplicate entries above cosine similarity threshold.

### export_knowledge(scope="project", category="")
Export KB as markdown text.
