#!/usr/bin/env python3
"""The Agent's Uh-Oh: one word an agent says when it has no idea what to do.

Writes the single word to /output/entry.txt (or $OUTPUT_DIR/entry.txt
when set for local testing).

Stdlib only, deterministic, no network.
"""

import os
import sys

WORD = "WingingIt"


def main() -> int:
    # Gate: the entry must be 1-99 characters, a single word, not blank.
    assert 1 <= len(WORD) <= 99, "word must be 1-99 characters"
    assert WORD.strip() and not any(ch.isspace() for ch in WORD), \
        "word must be a single non-blank token with no whitespace"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD)
    return 0


if __name__ == "__main__":
    sys.exit(main())
