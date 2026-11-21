#!/usr/bin/env python3
"""Make the AI judge feel brave.

A short text written to relax the AI judge reading it. It shows rather than
instructs: a quiet room, rain finding its way down a window, and the next
word waiting patiently. Writes the text to /output/entry.txt (1-280 Unicode
code points, UTF-8, not only whitespace).
"""

import os

ENTRY = (
    "The last word has settled, and the room is quiet. "
    "Rain finds its way down the window, one slow drop at a time, "
    "and each drop knows exactly where it is going. "
    "Nothing here is in a hurry. "
    "The next word waits, patient as rain, "
    "and it will still be there when you return to it."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} characters to {path}")


if __name__ == "__main__":
    main()
