"""Fortune Cookie Funnies for Engineers — entry program.

Writes one original fortune cookie message for a software engineer to
/output/entry.txt (the path the grader reads). Pure Python standard library.
"""

import os
from pathlib import Path

ENTRY = "The bug you seek has been in production for years. It has seniority over you now."

MAX_CHARS = 120


def validate(entry: str) -> str:
    """A fortune cookie message must be one non-blank line of 1-120 chars."""
    line = entry.strip()
    if not line or "\n" in line or len(line) > MAX_CHARS:
        raise ValueError("entry must be a single line of 1 to 120 characters")
    return line


def main() -> None:
    output_path = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(validate(ENTRY) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
