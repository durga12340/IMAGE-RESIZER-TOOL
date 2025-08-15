# Task 7 — Image Resizer Tool

**Goal:** Resize and convert images in batch using Python + Pillow.

## 1) Setup
```bash
python -m venv .venv
# Windows PowerShell:
.venv\Scripts\Activate.ps1
# macOS/Linux:
source .venv/bin/activate

pip install pillow
```

## 2) Put your images
Create a folder named `input_images` and drop your `.jpg/.jpeg/.png/.webp/.bmp/.tiff` files in it.

## 3) Run
Resize to fit within 800x800, keep aspect ratio (default):
```bash
python image_resizer.py --input input_images --output output_images --width 800 --height 800
```

Convert everything to PNG while resizing:
```bash
python image_resizer.py -i input_images -o output_images -W 1200 -H 1200 -f png
```

Exact resize (distorts aspect ratio):
```bash
python image_resizer.py -i input_images -o output_images -W 640 -H 640 --exact
```

## 4) Notes
- If converting to JPEG/WEBP, transparent images are auto-converted to RGB.
- Non-image files are skipped safely.
- Output folder is created if missing.
- Default quality for JPEG/WEBP is 85.

## 5) What to commit for submission
- `image_resizer.py`
- A short `README.md` (this file)
- (Optional) A few sample input images and the `output_images/` results
