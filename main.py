#!/usr/bin/env python3
"""Entry for make.fun bounty: one line, one laugh — the office joke.

The joke: the office coffee machine breaks, management responds with a
meeting about morale, and the punchline lands in the last few words —
the company was never running on strategy at all, just caffeine and
denial.

Prints the single-line office joke to stdout and also writes a copy to
the output directory (``/output/entry.txt`` by default, or
``$MAKEFUN_OUTPUT`` when set), verifying the written file by reading
it back. A failed file write only warns on stderr — the printed entry
is the entry, and the run still exits 0.

Python 3.13, stdlib only, deterministic: no network, clock, or randomness.
"""

import os
import sys

ENTRY = (
    "The office coffee machine broke, so management called a meeting "
    "about morale \u2014 turns out the only thing keeping this company "
    "running was caffeine and denial."
)

MIN_LENGTH = 1
MAX_LENGTH = 200


def validate(text: str) -> None:
    """Raise ValueError unless *text* is a valid single-line entry.

    Valid means: between MIN_LENGTH and MAX_LENGTH characters, no
    newline or carriage return anywhere, no leading or trailing
    whitespace, no control characters, and at least one letter — so a
    typo that empties the joke cannot slip through unnoticed.
    """
    if not MIN_LENGTH <= len(text) <= MAX_LENGTH:
        raise ValueError(
            f"entry must be {MIN_LENGTH}-{MAX_LENGTH} characters, "
            f"got {len(text)}"
        )
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in text):
        raise ValueError("entry must not contain control characters")
    if not any(ch.isalpha() for ch in text):
        raise ValueError("entry must contain at least one letter")


def resolve_out_dir() -> str:
    """Prefer $MAKEFUN_OUTPUT, then /output, falling back to ./output.

    Each candidate is probed with a write test first, so a directory
    that exists but is not writable is skipped instead of failing the
    run later.
    """
    candidates = [os.environ.get("MAKEFUN_OUTPUT"), "/output"]
    for candidate in candidates:
        if not candidate:
            continue
        try:
            os.makedirs(candidate, exist_ok=True)
            probe = os.path.join(candidate, ".write_probe")
            with open(probe, "w", encoding="utf-8") as f:
                f.write("ok")
            os.remove(probe)
            return candidate
        except OSError:
            continue
    fallback = os.path.join(os.getcwd(), "output")
    os.makedirs(fallback, exist_ok=True)
    return fallback


def write_and_verify(directory: str, text: str) -> None:
    """Write *text* to ``entry.txt`` in *directory* and read it back.

    Raises OSError on a failed write and RuntimeError when the bytes
    read back do not match what was written or fail validation.
    """
    path = os.path.join(directory, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    if os.path.getsize(path) != len(text.encode("utf-8")):
        raise RuntimeError("verification failed: written file size mismatch")
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    validate(written)
    if written != text:
        raise RuntimeError("verification failed: written entry does not match")


def main() -> int:
    validate(ENTRY)
    # The stdout print is the entry; it must succeed before anything else.
    print(ENTRY, flush=True)
    try:
        write_and_verify(resolve_out_dir(), ENTRY)
    except (OSError, RuntimeError) as exc:
        # The file copy is a convenience only; the entry is already
        # printed, so a failed write — or a verification mismatch —
        # must not fail the run.
        print(f"warning: could not write entry.txt: {exc}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
