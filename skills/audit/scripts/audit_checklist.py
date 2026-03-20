#!/usr/bin/env python3
import sys
import hashlib
from pathlib import Path
from datetime import datetime, timezone

BUILTIN_EXCLUDE_DIRS = {
    "node_modules", ".git", "dist", "build", "target", "vendor", "gen",
    "__pycache__", ".cache", ".turbo", ".next", ".nuxt", ".output",
    "coverage", "test-results", ".audit",
    ".claude", ".vscode", ".idea", ".vs",
}

BUILTIN_EXCLUDE_SUFFIXES = {
    ".lock", ".min.js", ".min.css", ".map",
    ".png", ".jpg", ".jpeg", ".gif", ".ico", ".svg", ".webp", ".avif",
    ".woff", ".woff2", ".ttf", ".eot", ".otf",
    ".wasm", ".so", ".dll", ".dylib", ".exe",
    ".zip", ".tar", ".gz", ".bz2", ".7z", ".rar",
    ".mp3", ".mp4", ".wav", ".ogg", ".webm",
    ".pdf", ".doc", ".docx", ".xls", ".xlsx",
}

BUILTIN_EXCLUDE_NAMES = {
    ".DS_Store", "Thumbs.db",
    "package-lock.json", "yarn.lock", "pnpm-lock.yaml",
    "Cargo.lock",
    "LICENSE", "CHANGELOG.md",
}

INCLUDE_SUFFIXES = {
    ".js", ".ts", ".tsx", ".jsx", ".vue", ".svelte",
    ".rs", ".go", ".py", ".rb", ".java", ".kt",
    ".css", ".scss", ".less", ".styl",
    ".html", ".htm",
    ".sql", ".graphql", ".gql",
    ".sh", ".bash", ".zsh", ".ps1",
    ".yaml", ".yml", ".toml", ".json",
    ".md",
}

AUDIT_DIR_NAME = ".audit"


def sha256_file(filepath: Path) -> str:
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def load_config(project_root: Path) -> dict:
    config_path = project_root / AUDIT_DIR_NAME / "config.yaml"
    config = {"exclude_dirs": [], "exclude_files": [], "module_map": {}}

    if not config_path.exists():
        return config

    current_key = None
    with open(config_path, "r", encoding="utf-8") as f:
        for line in f:
            stripped = line.rstrip()
            if not stripped or stripped.startswith("#"):
                continue

            if stripped.endswith(":") and not stripped.startswith(" "):
                current_key = stripped.rstrip(":")
                continue

            if current_key in ("exclude_dirs", "exclude_files"):
                trimmed = stripped.strip()
                if trimmed.startswith("- "):
                    val = trimmed[2:].strip().strip('"').strip("'")
                    config[current_key].append(val)

            elif current_key == "module_map":
                trimmed = stripped.strip()
                if ":" in trimmed:
                    k, v = trimmed.split(":", 1)
                    k = k.strip().strip('"').strip("'")
                    v = v.strip().strip('"').strip("'")
                    config["module_map"][k] = v

    return config


def is_excluded_dir(rel_parts: tuple, extra_dirs: list) -> bool:
    all_excludes = BUILTIN_EXCLUDE_DIRS | set(extra_dirs)
    for part in rel_parts:
        if part in all_excludes:
            return True
    return False


def should_include(filepath: Path, root: Path, config: dict) -> bool:
    rel = filepath.relative_to(root)
    parts = rel.parts

    if is_excluded_dir(parts, config.get("exclude_dirs", [])):
        return False

    rel_posix = rel.as_posix()
    for ef in config.get("exclude_files", []):
        if rel_posix == ef or filepath.name == ef:
            return False

    name = filepath.name
    if name in BUILTIN_EXCLUDE_NAMES:
        return False

    suffix = filepath.suffix.lower()
    if suffix in BUILTIN_EXCLUDE_SUFFIXES:
        return False

    if suffix not in INCLUDE_SUFFIXES:
        return False

    return True


def detect_module(rel_path: str, module_map: dict) -> str:
    normalized = rel_path.replace("\\", "/")

    for prefix in sorted(module_map.keys(), key=len, reverse=True):
        if normalized.startswith(prefix + "/") or normalized == prefix:
            return module_map[prefix]

    parts = normalized.split("/")
    top = parts[0] if parts else "root"

    if len(parts) > 1 and "." not in parts[1]:
        return f"{top}/{parts[1]}"

    if "." in top:
        return "root"

    return top


def load_yaml_simple(filepath: Path) -> dict:
    data = {"summary": {}, "modules": {}}
    current_module = None
    current_entry = None

    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            stripped = line.rstrip()
            if not stripped:
                continue

            if stripped.startswith("created:"):
                data["created"] = stripped.split('"')[1] if '"' in stripped else stripped.split(": ", 1)[1]
            elif stripped.startswith("  total:"):
                data["summary"]["total"] = int(stripped.split(":")[1].strip())
            elif stripped.startswith("  audited:") and "summary" in data:
                data["summary"]["audited"] = int(stripped.split(":")[1].strip())
            elif stripped.startswith("  pending:") and "summary" in data:
                data["summary"]["pending"] = int(stripped.split(":")[1].strip())
            elif stripped.startswith("  stale:") and "summary" in data:
                data["summary"]["stale"] = int(stripped.split(":")[1].strip())
            elif stripped.startswith("  modified:") and "summary" in data:
                data["summary"]["modified"] = int(stripped.split(":")[1].strip())
            elif stripped.startswith("  ") and stripped.endswith(":") and not stripped.strip().startswith("-"):
                name = stripped.strip().rstrip(":")
                if name not in ("summary", "modules", "created"):
                    current_module = name
                    if current_module not in data["modules"]:
                        data["modules"][current_module] = []
            elif stripped.strip().startswith("- path:"):
                val = stripped.split('"')[1] if '"' in stripped else stripped.split(": ", 1)[1]
                current_entry = {"path": val, "sha256": "", "status": "pending"}
                if current_module:
                    data["modules"][current_module].append(current_entry)
            elif stripped.strip().startswith("sha256:") and current_entry:
                current_entry["sha256"] = stripped.split('"')[1] if '"' in stripped else stripped.split(": ", 1)[1]
            elif stripped.strip().startswith("status:") and current_entry:
                current_entry["status"] = stripped.split(":")[1].strip()

    return data


def save_yaml(data: dict, filepath: Path):
    lines = []
    lines.append(f'created: "{data.get("created", "")}"')
    s = data.get("summary", {})
    lines.append("summary:")
    lines.append(f"  total: {s.get('total', 0)}")
    lines.append(f"  audited: {s.get('audited', 0)}")
    lines.append(f"  pending: {s.get('pending', 0)}")
    lines.append(f"  stale: {s.get('stale', 0)}")
    lines.append(f"  modified: {s.get('modified', 0)}")
    lines.append("")
    lines.append("modules:")

    for module in sorted(data.get("modules", {}).keys()):
        entries = data["modules"][module]
        lines.append(f"  {module}:")
        for e in entries:
            lines.append(f'    - path: "{e["path"]}"')
            lines.append(f'      sha256: "{e["sha256"]}"')
            lines.append(f'      status: {e["status"]}')

    filepath.write_text("\n".join(lines) + "\n", encoding="utf-8")


def recompute_summary(data: dict):
    counts = {"total": 0, "audited": 0, "pending": 0, "stale": 0, "modified": 0}
    for entries in data["modules"].values():
        for e in entries:
            counts["total"] += 1
            st = e["status"]
            if st in counts:
                counts[st] += 1
    data["summary"] = counts


def audit_dir(project_root: Path) -> Path:
    return project_root / AUDIT_DIR_NAME


def checklist_path(project_root: Path) -> Path:
    return audit_dir(project_root) / "checklist.yaml"


def cmd_init(project_root: Path):
    ad = audit_dir(project_root)
    ad.mkdir(parents=True, exist_ok=True)
    (ad / "modules").mkdir(exist_ok=True)

    config_path = ad / "config.yaml"
    if config_path.exists():
        print(f"config.yaml already exists at {config_path}")
        return

    config_path.write_text(
        "# Audit configuration\n"
        "# Project-specific exclude rules (in addition to built-in excludes)\n"
        "\n"
        "exclude_dirs:\n"
        "  # - \"some-generated-dir\"\n"
        "  # - \".vscode\"\n"
        "\n"
        "exclude_files:\n"
        "  # - \"some-specific-file.js\"\n"
        "\n"
        "# Map directory prefixes to module names\n"
        "# Longer prefixes take priority over shorter ones\n"
        "module_map:\n"
        "  # - \"ocs/bridge\": \"bridge\"\n"
        "  # - \"ocs/core\": \"bridge\"\n",
        encoding="utf-8",
    )

    print(f"Created {config_path}")
    print("Edit this file to add project-specific exclude rules and module mappings")


def cmd_generate(project_root: Path):
    ad = audit_dir(project_root)
    modules_dir = ad / "modules"
    cl = checklist_path(project_root)

    ad.mkdir(parents=True, exist_ok=True)
    modules_dir.mkdir(exist_ok=True)

    config = load_config(project_root)
    module_map = config.get("module_map", {})

    module_files: dict[str, list] = {}
    total = 0

    for filepath in sorted(project_root.rglob("*")):
        if not filepath.is_file():
            continue
        if not should_include(filepath, project_root, config):
            continue

        rel = filepath.relative_to(project_root).as_posix()
        module = detect_module(rel, module_map)
        h = sha256_file(filepath)

        if module not in module_files:
            module_files[module] = []
        module_files[module].append({"path": rel, "sha256": h, "status": "pending"})
        total += 1

    if total == 0:
        print("No source files found", file=sys.stderr)
        sys.exit(1)

    data = {
        "created": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "summary": {"total": total, "audited": 0, "pending": total, "stale": 0, "modified": 0},
        "modules": module_files,
    }

    save_yaml(data, cl)

    print(f"Generated {cl}")
    print(f"  Total files: {total}")
    print(f"  Modules: {len(module_files)}")
    for mod in sorted(module_files):
        print(f"    {mod}: {len(module_files[mod])} files")


def cmd_verify(project_root: Path):
    cl = checklist_path(project_root)
    if not cl.exists():
        print(f"ERROR: {cl} not found", file=sys.stderr)
        print("Run: python audit_checklist.py generate", file=sys.stderr)
        sys.exit(1)

    data = load_yaml_simple(cl)
    stats = {"audited": 0, "pending": 0, "stale": 0, "modified": 0, "missing": 0, "unchanged": 0}

    for module, entries in data["modules"].items():
        for e in entries:
            fp = project_root / e["path"]
            if not fp.exists():
                print(f"MISSING  {e['path']}")
                stats["missing"] += 1
                continue

            current_hash = sha256_file(fp)
            if current_hash != e["sha256"]:
                if e["status"] == "audited":
                    print(f"STALE    {e['path']}  (was audited, file changed)")
                    stats["stale"] += 1
                else:
                    print(f"MODIFIED {e['path']}  (was {e['status']}, file changed)")
                    stats["modified"] += 1
            else:
                stats[e["status"]] = stats.get(e["status"], 0) + 1
                stats["unchanged"] += 1

    print()
    print("=== Verification Summary ===")
    print(f"  Audited (ok):   {stats['audited']}")
    print(f"  Pending:        {stats['pending']}")
    print(f"  Stale:          {stats['stale']}")
    print(f"  Modified:       {stats['modified']}")
    print(f"  Missing:        {stats['missing']}")

    if stats["stale"] > 0 or stats["modified"] > 0 or stats["missing"] > 0:
        print()
        print("Action needed: run 'python audit_checklist.py refresh' to update statuses")
        sys.exit(2)

    if stats["pending"] == 0 and stats["audited"] > 0:
        print()
        print("All files audited")
        sys.exit(0)

    if stats["pending"] > 0:
        print()
        print(f"Audit in progress: {stats['pending']} files remaining")
        sys.exit(1)


def cmd_refresh(project_root: Path):
    cl = checklist_path(project_root)
    if not cl.exists():
        print(f"ERROR: {cl} not found", file=sys.stderr)
        sys.exit(1)

    data = load_yaml_simple(cl)
    stats = {"unchanged": 0, "stale": 0, "modified": 0, "missing": 0}

    for module, entries in data["modules"].items():
        for e in entries:
            fp = project_root / e["path"]
            if not fp.exists():
                print(f"MISSING  {e['path']}")
                stats["missing"] += 1
                continue

            current_hash = sha256_file(fp)
            if current_hash != e["sha256"]:
                old_status = e["status"]
                e["sha256"] = current_hash
                if old_status == "audited":
                    e["status"] = "stale"
                    print(f"STALE    {e['path']}")
                    stats["stale"] += 1
                elif old_status == "pending":
                    e["status"] = "modified"
                    print(f"MODIFIED {e['path']}")
                    stats["modified"] += 1
                else:
                    stats["modified"] += 1
            else:
                stats["unchanged"] += 1

    recompute_summary(data)
    save_yaml(data, cl)

    print()
    print("Refresh complete:")
    for k, v in stats.items():
        print(f"  {k.capitalize():12s} {v}")


def cmd_mark_audited(project_root: Path, target: str):
    cl = checklist_path(project_root)
    if not cl.exists():
        print(f"ERROR: {cl} not found", file=sys.stderr)
        sys.exit(1)

    data = load_yaml_simple(cl)
    changed = 0

    if target in data["modules"]:
        for e in data["modules"][target]:
            if e["status"] != "audited":
                fp = project_root / e["path"]
                if fp.exists():
                    e["sha256"] = sha256_file(fp)
                e["status"] = "audited"
                changed += 1
        recompute_summary(data)
        save_yaml(data, cl)
        print(f"Marked module '{target}' as audited ({changed} files)")
    else:
        found = False
        for module, entries in data["modules"].items():
            for e in entries:
                if e["path"] == target:
                    fp = project_root / e["path"]
                    if fp.exists():
                        e["sha256"] = sha256_file(fp)
                    e["status"] = "audited"
                    changed += 1
                    found = True
                    break
            if found:
                break

        if not found:
            print(f"ERROR: '{target}' not found as module or file path", file=sys.stderr)
            sys.exit(1)

        recompute_summary(data)
        save_yaml(data, cl)
        print(f"Marked '{target}' as audited")


def cmd_summary(project_root: Path):
    cl = checklist_path(project_root)
    if not cl.exists():
        print(f"ERROR: {cl} not found", file=sys.stderr)
        sys.exit(1)

    data = load_yaml_simple(cl)
    s = data["summary"]

    print("=== Audit Progress ===")
    print(f"  Total:    {s.get('total', 0)}")
    print(f"  Audited:  {s.get('audited', 0)}")
    print(f"  Pending:  {s.get('pending', 0)}")
    print(f"  Stale:    {s.get('stale', 0)}")
    print(f"  Modified: {s.get('modified', 0)}")

    total = s.get("total", 0)
    audited = s.get("audited", 0)
    if total > 0:
        pct = audited * 100 // total
        print(f"\n  Progress: {audited}/{total} ({pct}%)")

    print(f"\n  Modules:")
    for mod in sorted(data["modules"]):
        entries = data["modules"][mod]
        mod_audited = sum(1 for e in entries if e["status"] == "audited")
        mod_total = len(entries)
        status = "done" if mod_audited == mod_total else f"{mod_audited}/{mod_total}"
        print(f"    {mod}: {status}")


def cmd_pending(project_root: Path, module_filter: str = ""):
    cl = checklist_path(project_root)
    if not cl.exists():
        print(f"ERROR: {cl} not found", file=sys.stderr)
        sys.exit(1)

    data = load_yaml_simple(cl)
    count = 0

    for module in sorted(data["modules"]):
        if module_filter and module != module_filter:
            continue
        for e in data["modules"][module]:
            if e["status"] in ("pending", "modified", "stale"):
                print(f"[{e['status']:8s}] {module}/{e['path']}")
                count += 1

    print(f"\n{count} files remaining")


def main():
    if len(sys.argv) < 2:
        print("Usage: python audit_checklist.py <command> [project_root] [args]")
        print()
        print("Commands:")
        print("  init [root]                   Create default .audit/config.yaml")
        print("  generate [root]               Scan project and create checklist.yaml")
        print("  verify [root]                 Check sha256 of all files against checklist")
        print("  refresh [root]                Update sha256 and mark stale/modified")
        print("  mark <module|filepath> [root]  Mark module or file as audited (rehash)")
        print("  summary [root]                Print audit progress")
        print("  pending [module] [root]        List files needing audit")
        sys.exit(1)

    command = sys.argv[1]

    if command == "init":
        root = Path(sys.argv[2]) if len(sys.argv) > 2 else Path.cwd()
        cmd_init(root.resolve())

    elif command == "generate":
        root = Path(sys.argv[2]) if len(sys.argv) > 2 else Path.cwd()
        cmd_generate(root.resolve())

    elif command == "verify":
        root = Path(sys.argv[2]) if len(sys.argv) > 2 else Path.cwd()
        cmd_verify(root.resolve())

    elif command == "refresh":
        root = Path(sys.argv[2]) if len(sys.argv) > 2 else Path.cwd()
        cmd_refresh(root.resolve())

    elif command == "mark":
        if len(sys.argv) < 3:
            print("Usage: python audit_checklist.py mark <module|filepath> [root]", file=sys.stderr)
            sys.exit(1)
        target = sys.argv[2]
        root = Path(sys.argv[3]) if len(sys.argv) > 3 else Path.cwd()
        cmd_mark_audited(root.resolve(), target)

    elif command == "summary":
        root = Path(sys.argv[2]) if len(sys.argv) > 2 else Path.cwd()
        cmd_summary(root.resolve())

    elif command == "pending":
        module_filter = ""
        root = Path.cwd()
        if len(sys.argv) > 2:
            arg = sys.argv[2]
            if Path(arg).is_dir():
                root = Path(arg)
            else:
                module_filter = arg
                if len(sys.argv) > 3:
                    root = Path(sys.argv[3])
        cmd_pending(root.resolve(), module_filter)

    else:
        print(f"Unknown command: {command}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
