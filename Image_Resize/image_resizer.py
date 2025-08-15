import os
from PIL import Image

# ==============================
#  CONFIGURATION — CHANGE HERE
# ==============================
input_folder = "input_images"      # Folder with original images
output_folder = "output_images"    # Folder to save processed images
new_width = 800                    # Desired max width
new_height = 800                   # Desired max height
convert_to_format = None           # e.g. "PNG", "JPEG", "WEBP" or None to keep original
# ==============================

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Loop through all files in the input folder
for filename in os.listdir(input_folder):
    file_path = os.path.join(input_folder, filename)

    if not os.path.isfile(file_path):
        continue

    try:
        with Image.open(file_path) as img:
            # Resize the image (keeping aspect ratio)
            img.thumbnail((new_width, new_height))

            # Prepare save path
            if convert_to_format:
                save_name = os.path.splitext(filename)[0] + "." + convert_to_format.lower()
                save_path = os.path.join(output_folder, save_name)
                img = img.convert("RGB") if convert_to_format.upper() in ["JPEG", "JPG", "WEBP"] else img
                img.save(save_path, convert_to_format.upper())
            else:
                save_path = os.path.join(output_folder, filename)
                img.save(save_path)

            print(f"✅ Resized and saved: {os.path.basename(save_path)}")

    except Exception as e:
        print(f"⚠ Skipped {filename} — {e}")
