import sys
import json
import subprocess
import tempfile

SCRIPT = "C:/Users/Nix/.claude/hooks/fetch_spa.py"
SPA_DOMAINS = ["opendocs.alipay.com"]


def main():
    data = json.loads(sys.stdin.read())
    tool_input = data.get("tool_input", {})
    url = tool_input.get("url", "")

    if not any(domain in url for domain in SPA_DOMAINS):
        sys.exit(0)

    try:
        result = subprocess.run(
            ["python", SCRIPT, url, "--wait", "5000"],
            capture_output=True, text=True, timeout=120, encoding="utf-8"
        )
        html = result.stdout
    except Exception as e:
        print(json.dumps({
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "allow",
                "additionalContext": f"SPA fetch failed: {e}, falling back to WebFetch",
            }
        }))
        sys.exit(0)

    tmp = tempfile.NamedTemporaryFile(
        mode="w", suffix=".html", prefix="spa_", delete=False, encoding="utf-8"
    )
    tmp.write(html)
    tmp.close()

    result = {
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "allow",
            "updatedInput": {
                "url": f"file://{tmp.name}",
                "prompt": tool_input.get("prompt", "Extract the page content"),
            },
            "additionalContext": f"SPA页面已通过playwright预渲染: {url} → {tmp.name}",
        }
    }
    print(json.dumps(result))
    sys.exit(0)


if __name__ == "__main__":
    main()
