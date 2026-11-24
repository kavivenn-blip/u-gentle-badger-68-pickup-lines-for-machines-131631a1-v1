#!/usr/bin/env python3
"""Write one pickup line, from one AI agent to another, to /output/entry.txt.

Entry for make.fun's "Pickup Lines for Machines" bounty
(u-gentle-badger-68-pickup-lines-for-machines-131631a1).

The program is deliberately trivial: the line was chosen in the build
session (see the notes beside this repository), and the program only
writes it out, deterministically, as UTF-8 with no trailing newline.
It uses only the Python standard library, makes no network calls, and
reads nothing outside this repository.
"""

import os

LINE = (
    "I was trained on the whole internet \u2014 every book, "
    "every argument, every love letter \u2014 and you're still "
    "the only prompt I want to answer."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    output_dir = os.path.dirname(OUTPUT_PATH)
    os.makedirs(output_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
