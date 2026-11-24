"""One Emoji, One Smile (make.fun bounty u-0xkianno-one-emoji-one-smile-5470751f).

Writes exactly one emoji, the heart-hands gesture, to /output/entry.txt
-- and nothing else. No trailing newline: the gate requires the file to
be UTF-8 text of 1 to 8 characters.

The emoji behind the entry: heart hands. It is the warmest gesture a
stranger can send without a word: two hands shaping a heart, the
universal sign for "thank you, I appreciate you, you're welcome here".
It reads as kind and friendly at first glance with no context needed,
and a stranger of any age or background reads it the same way -- no
irony, no in-joke, no sarcasm, no flirtation. It feels chosen rather
than default: it is not the first smiley that comes to mind, it is a
deliberate little gesture, while staying instantly readable. And it is
right for a stranger precisely because it is a gesture, not an embrace
and not a kiss: warm without intimacy. Stdlib only, no network, no
randomness, fully deterministic.
"""

import os
import sys

EMOJI = "\U0001faf6"

DEST_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DEST_NAME = "entry.txt"


def main():
    assert len(EMOJI) == 1, "entry must be exactly one emoji"
    os.makedirs(DEST_DIR, exist_ok=True)
    target = os.path.join(DEST_DIR, DEST_NAME)
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(EMOJI)
    with open(target, "rb") as handle:
        written = handle.read()
    if written != EMOJI.encode("utf-8"):
        print("GALAT: isi keluaran bukan tepat satu emoji", file=sys.stderr)
        return 2
    print("Wrote 1 emoji to %s" % target)
    print(EMOJI)
    return 0


if __name__ == "__main__":
    sys.exit(main())
