import re

with open('index.html', 'r', encoding='utf-8', errors='replace') as f:
    content = f.read()

# Find all image sources
img_matches = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', content)
bg_matches = re.findall(r'url\(["\']?([^"\')\s]+)["\']?\)', content)

print("=== IMG SRC TAGS ===")
for src in img_matches:
    print(src)

print("\n=== CSS BACKGROUND URLs ===")
for url in bg_matches:
    if url.startswith('http') or url.startswith('/'):
        print(url)
