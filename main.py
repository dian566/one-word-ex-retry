#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""One Word From Your Ex — entry generator.

Writes a single word (max 24 characters) to /output/entry.txt.
The word is "Rebound": the one word that sums up what came after.
"""

import os
import sys

WORD = "Rebound"
MAX_LEN = 24


def main() -> int:
    if len(WORD) > MAX_LEN:
        print(f"word too long: {len(WORD)} > {MAX_LEN}", file=sys.stderr)
        return 1
    if " " in WORD or "\n" in WORD:
        print("word must be a single word", file=sys.stderr)
        return 1
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(WORD + "\n")
    print(f"wrote {out_path}: {WORD!r}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
