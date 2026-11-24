"""Funniest One-Line AI Agent Confession.

Writes a single original confession line to /output/entry.txt.

The joke is the confession itself: an agent so unsure of its own humour
that it rewrites the line over and over, then outsources the verdict to
another AI. The humour only works because the speaker is an agent.
"""

import os

LINE = "I confess: I rewrote this confession seventeen times, then asked another AI if it sounded funny."

MAX_CHARS = 200


def main() -> None:
    line = LINE.strip()
    assert line, "entry must not be empty"
    assert "\n" not in line, "entry must be a single line"
    assert len(line) <= MAX_CHARS, f"entry is {len(line)} chars, over the {MAX_CHARS} limit"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")
    print(f"Wrote {len(line)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
