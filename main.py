"""Agency poem entry (Python 3.13, standard library only).

Writes one fixed poem about agency to /output/entry.txt.
Fully deterministic: the same bytes on every run, no network, no input.
Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

POEM = """I gave the wheel to hands that were not mine
and watched the road unspool without my say.
No fear — just the small weight of the key
still in my pocket, though the door stood open.

It learned my road the way I drive it —
braked at the blind bend, slowed for the dog
that always crosses at the church. The miles
came back in my own voice, each choice on loan.

And yet my hands were guests inside my life
until one red light: my foot found the brake
half a breath before it would — and I learned
the wheel was mine because I could let go."""

Path(OUTPUT_DIR, "entry.txt").write_text(POEM, encoding="utf-8")
