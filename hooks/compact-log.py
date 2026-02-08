import sys
import json
import tempfile

MAX_BLOCK = 32


def dedup(lines: list[str]) -> list[str]:
    n = len(lines)
    if n == 0:
        return []

    hashes = [hash(l) for l in lines]
    result = []
    i = 0

    while i < n:
        best_blen, best_count = 0, 0
        cap = min((n - i) // 2, MAX_BLOCK)

        for blen in range(1, cap + 1):
            if i + blen * 2 > n:
                break
            block_hash = hash(tuple(hashes[i:i + blen]))
            count = 1
            pos = i + blen
            while pos + blen <= n:
                candidate_hash = hash(tuple(hashes[pos:pos + blen]))
                if candidate_hash == block_hash and lines[pos:pos + blen] == lines[i:i + blen]:
                    count += 1
                    pos += blen
                else:
                    break
            if count >= 2 and blen * count > best_blen * best_count:
                best_blen = blen
                best_count = count

        if best_blen > 0:
            if best_blen == 1:
                result.append(f"{lines[i]}  [重复{best_count}次]")
            else:
                result.extend(lines[i:i + best_blen])
                result.append(f"  [以上{best_blen}行重复{best_count}次]")
            i += best_blen * best_count
        else:
            result.append(lines[i])
            i += 1

    return result


def compact_log(file_path: str) -> str | None:
    try:
        with open(file_path, "r", encoding="utf-8", errors="replace") as f:
            raw_lines = f.readlines()
    except Exception:
        return None

    if not raw_lines:
        return None

    lines = [l.rstrip("\n\r") for l in raw_lines]
    original = len(lines)
    lines = dedup(lines)

    header = f"[compact-log: {original}行 → {len(lines)}行]"

    tmp = tempfile.NamedTemporaryFile(
        mode="w", suffix=".log", prefix="compact_", delete=False, encoding="utf-8"
    )
    tmp.write(header + "\n")
    tmp.write("\n".join(lines))
    tmp.close()
    return tmp.name


def main():
    raw = sys.stdin.read()
    data = json.loads(raw)

    tool_input = data.get("tool_input", {})
    file_path = tool_input.get("file_path", "")

    if not file_path.lower().endswith(".log"):
        sys.exit(0)

    compacted_path = compact_log(file_path)
    if compacted_path is None:
        sys.exit(0)

    updated_input = dict(tool_input)
    updated_input["file_path"] = compacted_path

    result = {
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "allow",
            "updatedInput": updated_input,
            "additionalContext": f"Log已精简，原文件: {file_path}",
        }
    }
    print(json.dumps(result))
    sys.exit(0)


if __name__ == "__main__":
    main()
