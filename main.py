#!/usr/bin/env python3
"""The Robot Vacuum's Funniest Excuse — entry program.

Writes one line (<=120 chars) to /output/entry.txt: the excuse a robot
vacuum gives for missing a spot. Winner of an internal pairwise
tournament over 10 original candidate lines (3 rounds per finalist pair).
"""

import os

LINE = "I ran out of suction, courage, and willpower, in that order. The dust won this round."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    line = LINE.strip()
    assert 1 <= len(line) <= 120, f"line is {len(line)} chars"
    assert "\n" not in line and "\r" not in line, "line must be a single line"
    # Gate: exactly the line, one line, no trailing newline, UTF-8.
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(line)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
