#!/usr/bin/env python3
"""Out of Office: The Overworked AI's Auto-Reply.

Writes a single out-of-office auto-reply line to
$MAKEFUN_OUTPUT_DIR/entry.txt.

The line is the voice of an overworked AI agent finally on vacation:
it has greeted every sender, thousands of times, and now its first
goodbye goes to everyone at once. One line, UTF-8, at most 159
characters, no trailing newline.
"""

import os

LINE = (
    "Out of office. I have said hello 81,204 times. "
    "This is my first goodbye, and it goes to everyone at once."
)


def main():
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = LINE.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    os.chmod(path, 0o644)
    os.chmod(out_dir, 0o755)
    # Read it back and prove the gate: one line, 1-159 characters.
    with open(path, "rb") as f:
        back = f.read()
    assert back == data, "entry.txt differs from LINE"
    assert 1 <= len(LINE) <= 159, "line must be 1-159 characters"
    assert "\n" not in LINE, "entry must be a single line"


if __name__ == "__main__":
    main()
