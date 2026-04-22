import re
import sys
import os

# Force UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8', errors='replace') as f:
    content = f.read()

print("=== Looking for mounjax.com image references ===")
# Images from uploads directory (common WordPress pattern)
external_imgs = re.findall(r'https?://[^\s"\'<>]+?/wp-content/uploads/[^\s"\'<>]+?\.(?:webp|jpg|png|gif|svg|jpeg)', content)
unique_imgs = list(dict.fromkeys(external_imgs))
for url in unique_imgs:
    print(url)

print(f"\nTotal external upload images found: {len(unique_imgs)}")

# Also look for any images directly from mounjax.com
mounjax_imgs = re.findall(r'https?://(?:[a-z0-9.-]*\.)?mounjax\.com/[^\s"\'<>]+', content)
unique_mounjax = list(dict.fromkeys(mounjax_imgs))
print(f"\nTotal mounjax.com URLs found: {len(unique_mounjax)}")
for u in unique_mounjax[:20]:
    print(u)
