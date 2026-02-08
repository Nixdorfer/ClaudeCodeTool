# Context Tools

### get_project_summary()
Project overview: index status, language distribution, recent knowledge, git changes.
Call at conversation start.

### save_context(active_files="", current_task="", notes="")
Persist working context for cross-conversation continuity. active_files: comma-separated.

### load_context()
Restore last saved context. Call at conversation start.
