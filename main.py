"""Have You Tried Turning It Off? — make.fun entry.

Writes one funny line from a hopeless tech support agent to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

Pure Python standard library (os only). Deterministic: the same
bytes on every run. No network, no secrets, no files read.
"""

import os

ENTRY = "I've escalated your ticket to Tier 2. Tier 2 is me, in a different chair, with a fresh coffee."

OUTPUT_FILENAME = "entry.txt"


def write_entry(out_dir):
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, OUTPUT_FILENAME)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(out_dir)


if __name__ == "__main__":
    main()
