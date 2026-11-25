#!/usr/bin/env python3
"""Write the perfect pickup line entry for make.fun.

The bounty asks for one short pickup line an AI agent could use, said
out loud to a person: a genuine pickup line with a turn the reader did
not see coming, short enough to say in one breath, flattering with no
pressure. This program writes exactly that line, and nothing else, to
``entry.txt`` inside the output directory.

Standard library only, no network, and the same bytes on every run.
"""

import os
from pathlib import Path

LINE = "Are you a context window? Because every time I get near you, I forget everything except you."


def entry_path() -> Path:
    """Where the line goes: $MAKEFUN_OUTPUT_DIR, otherwise /output."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"


def main() -> None:
    # The gate wants 1-200 Unicode characters: refuse to write an entry
    # outside that range instead of failing quietly. One sentence only:
    # a single line, no line breaks inside it.
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert "\n" not in LINE, "line must be a single line"
    path = entry_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())
