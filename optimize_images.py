import os
from PIL import Image
import glob

# Path to images
img_dir = 'C:\\Users\\Pedro\\.gemini\\antigravity\\scratch\\authentic-mexican-flavors\\assets\\img'

# Find all png and jpg images
images = glob.glob(os.path.join(img_dir, '*.png')) + glob.glob(os.path.join(img_dir, '*.jpg'))

for img_path in images:
    if 'menu-' in img_path:
        try:
            with Image.open(img_path) as img:
                # Resize image to max 400x400 to save space while keeping it sharp enough for retina displays
                img.thumbnail((400, 400), Image.Resampling.LANCZOS)
                
                # Convert to WebP
                webp_path = os.path.splitext(img_path)[0] + '.webp'
                img.save(webp_path, 'WEBP', quality=80)
                print(f"Optimized: {os.path.basename(webp_path)}")
        except Exception as e:
            print(f"Error processing {img_path}: {e}")
