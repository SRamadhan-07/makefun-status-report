#!/usr/bin/env python3
"""Status Report Comedy Sprint — entry program.

The entry is the funniest line an AI agent would put in its weekly
status report to its human. This program writes that one line to
/output/entry.txt (UTF-8, no trailing newline).
"""

import os
from pathlib import Path

STATUS_LINE = (
    "Weekly status: all tasks complete, zero errors, one blocker "
    "remaining — you keep scheduling 'quick syncs' that are neither."
)


def main() -> None:
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out.mkdir(parents=True, exist_ok=True)
    entry_file = out / "entry.txt"
    # No trailing newline: the scored text is the status line alone,
    # 123 characters against a 200-character ceiling.
    entry_file.write_text(STATUS_LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
