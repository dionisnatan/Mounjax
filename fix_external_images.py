import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8', errors='replace') as f:
    content = f.read()

original_len = len(content)

# Fix 1: Replace the external banner1.webp URL to local
content = content.replace(
    'https://mounjax.com/wp-content/uploads/2025/06/banner1.webp',
    'images/banner1.webp'
)

# Fix 2: Replace the external logo/favicon images
content = content.replace(
    'https://mounjax.com/wp-content/uploads/2025/06/cropped-cone_monjax_1.webp',
    'images/cropped-cropped-cone_monjax_1-180x180.webp'
)

content = content.replace(
    'https://mounjax.com/wp-content/uploads/2025/06/cropped-cropped-cone_monjax_1-270x270.webp',
    'images/cropped-cropped-cone_monjax_1-180x180.webp'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Done! File size: {original_len} -> {len(content)} bytes")
print("Fixed 3 external image URLs to local paths")
