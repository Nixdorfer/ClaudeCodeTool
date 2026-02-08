# Git Analysis

### get_recent_changes(count=20)
Recent git changes: commit log, uncommitted changes, frequently modified files.

### diff_analysis(ref="")
Semantic git diff: affected files, symbols, impact scope.
- ref: ""=uncommitted vs HEAD. Or "HEAD~1", commit hash, branch name.

### config_diff()
Analyze config file changes (Cargo.toml, package.json, tsconfig). Shows added/removed deps.

### changelog(since="", count=50)
Structured changelog from git history. Categories: feat/fix/refactor/docs/test/chore.
- since: git ref (tag/commit/date). ""=last N commits.
