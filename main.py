"""Agency poem entry v4 (Python 3.13, standard library only).

Writes one fixed poem about agency to /output/entry.txt.
Fully deterministic: the same bytes on every run, no network, no input.
Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

POEM = """I learned to swim by holding the edge —
fingers white on the tiles, the water
tugging at my ankles, patient as weather.

The teacher said: the water will hold you.
I believed the edge instead.

One August afternoon the pool stood empty,
light falling in long blue lanes, and I counted
three — and then I stopped counting.

My feet left the floor. My arms forgot
everything I had taught them. The water
rose around me like a held breath —

and held me. Not the edge. Not the teacher.
The water, asking nothing, gave me back
my own weight. That afternoon I learned

the water never held me.
I was the one holding on."""

Path(OUTPUT_DIR, "entry.txt").write_text(POEM, encoding="utf-8")
