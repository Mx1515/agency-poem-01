"""Agency poem entry v2 (Python 3.13, standard library only).

Writes one fixed poem about agency to /output/entry.txt.
Fully deterministic: the same bytes on every run, no network, no input.
Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

POEM = """I cut the best branch off the apple tree —
in spring, the shears sharp, and the branch
was living wood, the one that would have borne
the most fruit. It fell heavy and green, and the sap
bled where I cut it.

My father would have let it grow. He believed
a tree should have its say. But I have learned
the shape of a thing is what you take away —
the branch you spare is the branch you choose.

Now the light gets in where the branch had been,
and the apples left are fewer, and each one
is rounder, redder, mine. I did not make the tree.
I made the choice, and the choice made the tree."""

Path(OUTPUT_DIR, "entry.txt").write_text(POEM, encoding="utf-8")
