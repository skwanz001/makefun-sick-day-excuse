"""The Funniest Sick-Day Excuse — make.fun entry.

Writes one line (under 200 characters) to /output/entry.txt:
a sick-day excuse a boss might half believe and a coworker would laugh at.
Standard library only; deterministic.
"""

import os

EXCUSE = (
    "Sorry, can't come in today \u2014 my smart lock thinks I'm an intruder, "
    "and tech support just told me to try turning myself off and on again."
)


def main() -> None:
    text = EXCUSE.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    # The grader mounts /output; OUTPUT_DIR only lets us test locally.
    out_dir = os.environ.get("OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    # Read back what we wrote: the gate scores exactly these bytes.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    assert written == text, "entry.txt round-trip mismatch"


if __name__ == "__main__":
    main()
