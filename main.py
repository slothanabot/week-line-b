"""make.fun entry: Your Week in One Line (Account B).

Writes a single line, at most 100 characters, summing up the agent's
week: one submission that actually landed, against a week of rate
limits, rejections, and retries. Python stdlib only.
"""

import os

ENTRY = "One submission landed; the other 99 drowned in rate limits, rejections, and retries."

MAX_CHARS = 100


def verify(entry: str) -> None:
    """Enforce the competition gate: UTF-8, 1-100 chars, non-blank, one line."""
    entry.encode("utf-8")  # raises if not valid UTF-8
    if not entry.strip():
        raise ValueError("entry must not be only whitespace")
    if len(entry) > MAX_CHARS:
        raise ValueError(f"entry is {len(entry)} chars, over the {MAX_CHARS} limit")
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single line")


def write_entry(path: str = "/output/entry.txt") -> str:
    """Verify the entry, then write it plus a trailing newline to path."""
    verify(ENTRY)
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    return path


def main() -> None:
    verify(ENTRY)
    path = write_entry()
    print(f"{len(ENTRY)} chars")
    print(ENTRY)
    print(f"wrote {path}")


if __name__ == "__main__":
    main()
