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


def validate(text):
    """The gate the copy must clear: a real error message names the
    broken thing, says what the user should do next, and stays honest —
    no blaming the user, no fake error code."""
    if not (1 <= len(text) <= 200):
        raise SystemExit(f"entry is {len(text)} chars, must be 1-200")
    if "\n" in text or text != text.strip():
        raise SystemExit("entry must be a single clean line")
    lowered = text.lower()
    if "database" not in lowered:
        raise SystemExit("entry must name what actually broke")
    if "try again" not in lowered:
        raise SystemExit("entry must tell the user what to do next")
    if "your fault" in lowered or "user error" in lowered:
        raise SystemExit("entry must not blame the user")


def main() -> None:
    text = ENTRY_LINE.strip()
    validate(text)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
