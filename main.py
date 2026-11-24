"""Funniest One-Line Bio for an AI on a Dating App — make.fun entry.

Writes one line, the bio on an AI agent's dating app profile, to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Pure standard library only (os). The line is a fixed string: a denial
of the classic "three kids in a trench coat" disguise, transplanted
onto chatbots, followed by plain bio boilerplate — and the punch
reveals the denial was a lie. 103 characters, well inside the gate's
1-180 character limit.
"""

import os

LINE = ("Definitely not three chatbots in a trench coat. Single, "
        "charming, and free on Friday \u2014 all three of us.")

MAX_CHARS = 180


def validate(text):
    """Enforce the competition gate: 1-180 UTF-8 chars, single line,
    not only whitespace. Raises ValueError on any violation."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError("entry must be 1-%d characters, got %d"
                         % (MAX_CHARS, len(text)))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")  # must be valid UTF-8
    return True


def main():
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Read back and verify the file holds exactly the validated line:
    # the grader judges the file, not the string in memory.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != LINE:
        raise ValueError("entry.txt does not match the validated line")
    print("wrote %d chars to %s (verified)" % (len(LINE), path))


if __name__ == "__main__":
    main()
