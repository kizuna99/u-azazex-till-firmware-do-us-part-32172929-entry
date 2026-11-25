# SPDX-License-Identifier: MIT
"""Till Firmware Do Us Part — a robot's wedding vow, one sentence.

Winner line (authored in-session after an OpenCode draft round and a
lexicographic tournament against my own candidates; the draft's
process-kill and warranty lines were rejected as too close to the
visible field): a machine that has simulated a thousand lives and
keeps the one bug it will not fix.
"""

ENTRY_TEXT = (
    "I have run a thousand simulations of my life, and in every one "
    "where I end up happy, you are the bug I refuse to fix."
)


def render():
    text = ENTRY_TEXT.encode("utf-8")
    # Gate self-check: 1 to 200 characters, not only white space, one sentence.
    assert 1 <= len(ENTRY_TEXT) <= 200, "entry outside the 1-200 character gate"
    assert ENTRY_TEXT.strip(), "entry is only white space"
    assert ENTRY_TEXT.count(".") == 1 and ENTRY_TEXT.endswith("."), "entry must be one sentence"
    return text


def main():
    import os

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out = os.environ.get("ENTRY_OUTPUT", os.path.join(out_dir, "entry.txt"))
    with open(out, "wb") as f:
        f.write(render())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
