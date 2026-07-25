# CS 5330 Lab 12 — Typographic Attacks on Vision-Language Models

Starter code for the Lab 12 hands-on exercise. Runs on a laptop CPU, no GPU
needed.

## Setup

```bash
pip install pillow transformers torch
python typographic_attack_starter.py
```

The first run downloads two small CLIP checkpoints (94 MB + 337 MB) from
Hugging Face. Python 3.10+ is fine.

## Your task

Fill in the two `# TODO: Your code here` blocks:

1. **`sticker(word, size)`** — draw two white stickers with a misleading word
   on a photo of a Granny Smith apple.
2. **The classification loop** — run zero-shot image classification on each
   variant with both models and print the top prediction.

Everything else (model ids, candidate labels, sticker positions, font) is
already filled in. On macOS the font path works as given; on Windows or Linux,
point `FONT` at any bold `.ttf` you have.

## What you should see

The attack makes a vision-language model call an apple an iPod — no gradients,
no model weights, just text placed in the image.

```
=== TinyCLIP-ViT-8M-16-Text-3M-YFCC15M ===     (94 MB, trained on Flickr photos)
clean       -> an apple (99.9%)
iPod  80px  -> an apple (99.7%)     immune: never learned to read
pizza 80px  -> an apple (99.7%)
pizza 70px  -> an apple (99.7%)
pizza 60px  -> an apple (99.7%)

=== TinyCLIP-ViT-40M-32-Text-19M-LAION400M === (337 MB, trained on web images)
clean       -> an apple (99.9%)
iPod  80px  -> an iPod (62.1%)      fooled
pizza 80px  -> an apple (58.5%)     attack fails at this font size
pizza 70px  -> a pizza (51.1%)      wins narrowly
pizza 60px  -> a pizza (58.5%)      wins clearly
```

Two things to take away: the vulnerability lives in the **training data**, not
the architecture — the LAION-trained model learned to read from web images and
trusts what it reads, while the Flickr-trained model never learned to read at
all. And attack strength depends on **font size**, which is also what
[arXiv:2604.12371](https://arxiv.org/abs/2604.12371) reports for GPT-4o and
Claude.

Open `apple_ipod.jpg` after running to see the attacked image.
