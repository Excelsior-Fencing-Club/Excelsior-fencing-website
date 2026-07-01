"""Resize and compress JPEGs for news posts (requires Pillow: pip install Pillow)."""

from PIL import Image, ImageOps
import os
import sys

folder = sys.argv[1] if len(sys.argv) > 1 else "."
max_edge = int(sys.argv[2]) if len(sys.argv) > 2 else 1600
quality = int(sys.argv[3]) if len(sys.argv) > 3 else 82

for name in sorted(f for f in os.listdir(folder) if f.lower().endswith(".jpg")):
    path = os.path.join(folder, name)
    before = os.path.getsize(path)
    with Image.open(path) as im:
        im = ImageOps.exif_transpose(im)
        im = im.convert("RGB")
        w, h = im.size
        scale = max_edge / max(w, h)
        if scale < 1:
            im = im.resize((round(w * scale), round(h * scale)), Image.Resampling.LANCZOS)
        im.save(path, "JPEG", quality=quality, optimize=True, progressive=True)
    after = os.path.getsize(path)
    with Image.open(path) as im:
        print(f"{name}: {before:,} -> {after:,} bytes, {im.size[0]}x{im.size[1]}")
