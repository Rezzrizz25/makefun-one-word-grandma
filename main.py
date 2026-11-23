#!/usr/bin/env python3
"""One Word From Grandma — the single word Grandma would text about AI.

The word: "thingamabob".

Why this word: it is the warm, slightly baffled name a grandma gives a
gadget she cannot name — exactly how she would text about AI to a
grandchild. It is funny in one word with no caption, it is tied to the
machine (her name for the mysterious new device), and it is a fresh pick:
the field is crowded with typo jokes (robit, robut, computor, chatgbt)
and the obvious gadget words (thingamajig, doohickey, contraption,
whatchamacallit, newfangled, witchcraft), while thingamabob — the
grandma-iest of them all — was still free.

Writes exactly that one word to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os

WORD = "thingamabob"

# The gate (competition.yaml): /output/entry.txt must be UTF-8 text of
# 1 to 30 characters, not only white space. Fail loudly rather than
# write something the gate would refuse.
assert 1 <= len(WORD) <= 30, "word must be 1-30 characters"
assert len(WORD.split()) == 1, "entry must be exactly one word"
assert WORD.strip() == WORD, "no leading or trailing whitespace"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
