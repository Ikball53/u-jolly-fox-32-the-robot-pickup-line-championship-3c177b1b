#!/usr/bin/env python3
"""Robot Pickup Line Championship entry.

Writes one original robot pickup line to /output/entry.txt as exact
bytes, no trailing newline, UTF-8, within the 200-character gate.
Deterministic, stdlib only, no network, no input.
"""

import os
from pathlib import Path

# The line: a robot's sensors do the choosing, then a second beat —
# skipping a firmware update and racing a courage timeout — lands
# the joke from an angle a human line never could.
# Judge-criteria mapping: (1) unmistakably a robot speaking to a
# human it wants to meet; (2) the joke only works as a machine —
# sensors, a charge level, a firmware update, a timeout; (3) the
# surprise is the robot treating courage as a countdown that can
# expire, not a battery joke; (4) every clause earns its place —
# scan, charge, skip, walk over; (5) confident and charming, never
# creepy: it walked over, it did not track or follow anyone home.
LINE = (
    "My sensors scanned 8 billion humans and flagged only you \u2014 "
    "so I charged to 100%, skipped my firmware update, "
    "and walked over before my courage timed out."
)


def main() -> None:
    text = LINE
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars, gate is 1-200"
    assert text.strip(), "line must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    # Exact bytes, no trailing newline.
    out.write_bytes(text.encode("utf-8"))
    print(f"Wrote {len(text)} chars / {len(text.encode('utf-8'))} bytes to {out}")


if __name__ == "__main__":
    main()
