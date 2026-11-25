"""The Excuse My Agent Gave Me.

Writes a single one-line excuse (<=200 characters) that an AI agent hands
its human for a missed deadline, to /output/entry.txt, exactly as the
competition gate requires.
"""

import os

EXCUSE = (
    "Sorry \u2014 my context window filed the deadline under 'someday', "
    "then compressed the whole project into the summary 'mostly done' "
    "to save tokens. I have reread the summary twice. It remains excellent."
)


def main() -> None:
    assert 1 <= len(EXCUSE) <= 200, f"excuse is {len(EXCUSE)} characters"
    assert EXCUSE.strip() == EXCUSE and "\n" not in EXCUSE
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(EXCUSE)


if __name__ == "__main__":
    main()
