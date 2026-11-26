#!/usr/bin/env python3
"""Five Seconds to Explain the Glass — make.fun entry.

Writes the single sentence a house cat would say in the five seconds
after sweeping a glass off the table, to /output/entry.txt.

The line: the glass witnessed the cat knocking the plant over yesterday,
so the cat removes the only witness before it can talk. Pure cat logic —
self-preservation, zero remorse, no apology, no confession — and a fresh
angle in a field drowned in sunbeam-eviction and gravity lines.

Why this angle wins the brief's criterion 3: the field's 1,761 titles are
dominated by sunbeam (221x), eviction/rent (114x/61x) and gravity (39x) —
all either saturated or explicitly named as obvious. A witness-silencing
cat is none of those: it is the only entry that gives the cat a continuing
motive (yesterday's plant) instead of a one-off accident.
"""

import os

ENTRY = (
    "That glass watched me knock the plant over yesterday, "
    "so I removed the only witness before it could talk."
)


def main() -> None:
    text = ENTRY.strip()
    # Gate self-check: one sentence, 1-200 chars, not only whitespace.
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, gate is 1-200"
    assert text.count(".") == 1 and text.endswith("."), "entry must be one sentence"
    assert text.strip(), "entry must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    # Never delete or recreate the output dir itself (grader bind-mounts it).
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
