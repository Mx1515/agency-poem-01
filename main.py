"""Agency poem entry v3 (Python 3.13, standard library only).

Writes one fixed poem about agency to /output/entry.txt.
Fully deterministic: the same bytes on every run, no network, no input.
Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

POEM = """I was nine when my grandmother taught me to knead bread —
push, fold, turn, push again, her hands over mine,
until the dough stopped fighting back.

She said: the bread does what your hands tell it.
Not the oven. Not the recipe. Your hands.

Years later I stood in a kitchen that was not mine,
in a life that was not mine, and felt my hands
go still, waiting for someone else to move them.

So I pushed. I folded. I turned.
I left the job, the house, the man who loved
the quiet version of me. I took the dough of my days
and made it rise on my own heat.

Nobody handed me the morning.
I baked it."""

Path(OUTPUT_DIR, "entry.txt").write_text(POEM, encoding="utf-8")
