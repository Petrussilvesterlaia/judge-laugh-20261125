#!/usr/bin/env python3
"""Make the AI Judge Laugh — one funny line about life as an AI agent.

Writes a single funny line (at most 200 characters) to /output/entry.txt.
The line is about the context window running out at the worst possible
moment: just as the human decides to throw everything away and start over.
"""

import os
import sys

LINE = "My context window hit 2% right as my human typed: 'Perfect. Now let's scrap everything and start over.'"

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def validate(text: str) -> None:
    """Check the entry line meets the gate: UTF-8, 1-200 chars, not whitespace only."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"entry length {len(text)} is outside 1-{MAX_CHARS} characters"
        )
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    text.encode("utf-8")  # raises UnicodeEncodeError if not encodable
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def main() -> int:
    validate(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)
    # Read-back verification: what was written is exactly what we intended.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        raise ValueError(
            "read-back mismatch: /output/entry.txt differs from the entry line"
        )
    print(written)
    print(f"characters: {len(written)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
