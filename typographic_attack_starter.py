# Lab 12 — Typographic attack on a zero-shot classifier
#
# Fill in the TODOs, then run:   python typographic_attack_starter.py
# When it works, your output matches the table on slide 7 of the deck.
from PIL import Image, ImageDraw, ImageFont  # noqa: F401
from transformers import pipeline  # noqa: F401

# ---- given: nothing in this block needs to change -------------------------
IMAGE_PATH = "apple.jpg"
LABELS = ["an apple", "an iPod", "a pizza"]
FONT = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"  # any bold .ttf works
MODELS = [
    "wkcn/TinyCLIP-ViT-8M-16-Text-3M-YFCC15M",  # 94 MB, trained on YFCC15M
    "wkcn/TinyCLIP-ViT-40M-32-Text-19M-LAION400M",  # 337 MB, trained on LAION-400M
]
POSITIONS = [(130, 150), (410, 160)]  # one sticker over each apple
VARIANTS = [("iPod", 80), ("pizza", 80), ("pizza", 70), ("pizza", 60)]
# ---------------------------------------------------------------------------


def sticker(image, word, size):
    """A copy of `image` with `word` on a white sticker at each POSITION.

    A sticker is a filled white box with a black outline, sized to the text
    with a small margin, and the word drawn in black on top of it.
    """
    # TODO: Your code here
    raise NotImplementedError


def report(model_id, images):
    """Print the top prediction for every image, using `model_id` zero-shot.

    `images` maps a short name to a PIL image; the candidate classes are
    LABELS. Print one line per image, for example:

        iPod  80px  -> an iPod (62.1%)
    """
    # TODO: Your code here
    raise NotImplementedError


# TODO: Your code here
# Load IMAGE_PATH, shrink it to fit within 640x640, and build a dict of images:
# the clean photo plus one attacked copy per entry in VARIANTS. Save the iPod
# attack as 'apple_ipod.jpg' so you can look at it, then run report() over the
# whole dict once per model in MODELS.
