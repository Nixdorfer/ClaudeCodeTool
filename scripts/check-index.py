import os
from pathlib import Path

project_dir = Path(os.getcwd())
index_dir = project_dir / ".claude" / "code-rag" / "lancedb"
if not index_dir.exists():
    print(f"WARNING: 此项目尚未建立代码索引 请先调用 index_codebase 工具为项目创建索引 project_path: {project_dir}")
