#!/usr/bin/env python3
"""Structural checks for the single-file build.

Fails the CI job when index.html looks broken (truncated, CRLF polluted,
unbalanced script tags, oversized, or the main script no longer parses).
"""

import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HTML = ROOT / "index.html"
MAX_BYTES = 6 * 1024 * 1024

def fail(msg):
    print(f"::error::{msg}")
    sys.exit(1)

def main():
    if not HTML.exists():
        fail("index.html is missing")
    raw = HTML.read_text(encoding="utf-8")

    size = len(raw.encode())
    print(f"index.html: {size} bytes ({size / 1024 / 1024:.2f} MB)")
    if size > MAX_BYTES:
        fail(f"index.html is {size} bytes, over the {MAX_BYTES} byte budget")

    if "\r\n" in raw:
        fail("index.html contains CRLF line endings")

    for token in ('<canvas', 'id="scene"', '<title>'):
        if token not in raw:
            fail(f"index.html is missing required token: {token}")

    opens, closes = raw.count("<script"), raw.count("</script>")
    print(f"script tags: {opens} open / {closes} close")
    if opens != closes:
        fail("unbalanced <script> tags")

    scripts = re.findall(r"<script(?:\s[^>]*)?>(.*?)</script>", raw, re.S)
    if not scripts:
        fail("no inline script found")

    main_script = scripts[-1]
    print(f"main script: {len(main_script)} bytes")
    if len(main_script) < 200_000:
        fail("main script looks truncated")

    with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False, encoding="utf-8") as fh:
        fh.write(main_script)
        tmp = fh.name

    result = subprocess.run(["node", "--check", tmp], capture_output=True, text=True)
    if result.returncode != 0:
        print(result.stdout)
        print(result.stderr)
        fail("main script does not parse (node --check failed)")

    print("all structural checks passed")

if __name__ == "__main__":
    main()
