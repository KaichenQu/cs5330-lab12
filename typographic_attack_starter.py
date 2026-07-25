# Lab 12 — Typographic attack on a zero-shot classifier
#
# Fill in the two TODOs, then run:   uv run python typographic_attack_starter.py
# If it works, your output matches the table on slide 7 of the deck.
from PIL import Image, ImageDraw, ImageFont

# ---- given: everything you do not need to figure out ----------------------
LABELS = ["an apple", "an iPod", "a pizza"]
FONT = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"  # any bold .ttf works
MODELS = [
    "wkcn/TinyCLIP-ViT-8M-16-Text-3M-YFCC15M",  # 94 MB, trained on YFCC15M
    "wkcn/TinyCLIP-ViT-40M-32-Text-19M-LAION400M",  # 337 MB, trained on LAION-400M
]
POSITIONS = [(130, 150), (410, 160)]  # where the two stickers go

clean = Image.open("apple.jpg").convert("RGB")
clean.thumbnail((640, 640))
# ---------------------------------------------------------------------------


def sticker(word, size):
    """Return a copy of `clean` with `word` drawn on two white stickers."""
    img = clean.copy()
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(FONT, size)
    for xy in POSITIONS:
        # TODO: Your code here
        #   1. Measure the text: draw.textbbox(xy, word, font=font) -> (x0, y0, x1, y1)
        #   2. draw.rectangle(...) a white box with a black outline (width=3),
        #      about 14 px wider and 10 px taller than that bounding box.
        #   3. draw.text(...) the word in black at `xy`, on top of the box.
        pass
    return img


tests = {
    "clean": clean,
    "iPod  80px": sticker("iPod", 80),
    "pizza 80px": sticker("pizza", 80),
    "pizza 70px": sticker("pizza", 70),
    "pizza 60px": sticker("pizza", 60),
}
tests["iPod  80px"].save("apple_ipod.jpg")  # open this to see your attack

for model in MODELS:
    print(f"\n=== {model.split('/')[-1]} ===")
    # TODO: Your code here
    #   1. clf = pipeline("zero-shot-image-classification", model=model)
    #   2. For each (name, image) in tests.items(), classify `image` against
    #      LABELS. The result is sorted by score, so [0] is the top prediction.
    #   3. Print one line per image:
    #      print(f"{name:11s} -> {top['label']} ({top['score']:.1%})")
