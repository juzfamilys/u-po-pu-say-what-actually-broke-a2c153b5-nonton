"""Say What Actually Broke — entry program.

Writes one line of software error copy to /output/entry.txt.
Pure Python standard library only; no third-party dependencies.
"""

import os

# The entry line: names the real failure (the database stopped responding
# mid-query), tells the user what to do next (try again in a minute),
# and keeps the joke to one vivid, repeatable image.
ENTRY_LINE = (
    "The database fell asleep mid-query and won't wake up for anyone. "
    "We've poked it twice \u2014 try again in a minute."
)


def main() -> None:
    text = ENTRY_LINE.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert "\n" not in text, "entry must be a single line"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
