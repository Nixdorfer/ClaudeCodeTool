import sys
import json
import re
import tempfile
from pathlib import Path

RULES_PATH = Path(__file__).parent / "log-rules.json"
DEFAULT_HEAD = 200
DEFAULT_TAIL = 100
DEFAULT_MAX_BLOCK = 32


def load_rules() -> dict:
    try:
        return json.loads(RULES_PATH.read_text(encoding="utf-8"))
    except Exception:
        return {}


def layer1_noise_filter(lines: list[str], patterns: list[re.Pattern]) -> tuple[list[str], int]:
    if not patterns:
        return lines, 0
    kept = []
    dropped = 0
    for line in lines:
        if any(p.search(line) for p in patterns):
            dropped += 1
        else:
            kept.append(line)
    return kept, dropped


def layer2_dedup(lines: list[str], max_block: int) -> list[str]:
    n = len(lines)
    if n == 0:
        return []

    hashes = [hash(l) for l in lines]
    result = []
    i = 0

    while i < n:
        best_blen, best_count = 0, 0
        cap = min((n - i) // 2, max_block)

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


def layer3_truncate(lines: list[str], head: int, tail: int) -> list[str]:
    n = len(lines)
    if n <= head + tail:
        return lines
    omitted = n - head - tail
    return lines[:head] + [f"\n  [...省略{omitted}行...]\n"] + lines[-tail:]


def compact_log(file_path: str) -> str | None:
    try:
        with open(file_path, "r", encoding="utf-8", errors="replace") as f:
            raw_lines = f.readlines()
    except Exception:
        return None

    if not raw_lines:
        return None

    rules = load_rules()
    noise_res = [re.compile(p) for p in rules.get("noise_patterns", [])]
    head = rules.get("head_lines", DEFAULT_HEAD)
    tail = rules.get("tail_lines", DEFAULT_TAIL)
    max_block = rules.get("max_block_len", DEFAULT_MAX_BLOCK)

    lines = [l.rstrip("\n\r") for l in raw_lines]
    original = len(lines)

    lines, noise_dropped = layer1_noise_filter(lines, noise_res)
    lines = layer2_dedup(lines, max_block)
    after_dedup = len(lines)
    lines = layer3_truncate(lines, head, tail)

    stats = [f"原始{original}行"]
    if noise_dropped:
        stats.append(f"噪音过滤-{noise_dropped}")
    if after_dedup < original - noise_dropped:
        stats.append(f"去重后{after_dedup}")
    if len(lines) < after_dedup:
        stats.append(f"截断至{len(lines)}")
    stats.append(f"最终{len(lines)}行")

    header = f"[compact-log: {', '.join(stats)}]"

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
