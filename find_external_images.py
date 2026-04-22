import re

with open('index.html', 'r', encoding='utf-8', errors='replace') as f:
    content = f.read()

# The hero background is likely set by Elementor via JS from the data-settings attribute
# Let's look at the raw HTML of the first container (hero section)
# and find data-settings that have image URLs

# Look for data-settings with "url" in them
settings_matches = re.finditer(r'data-settings=.{0,2000}', content[:100000])
for m in settings_matches:
    text = m.group(0)
    if 'url' in text.lower() or 'image' in text.lower() or 'background' in text.lower():
        print(text[:600])
        print("---")

print("\n\n=== Looking for mounjax.com image references ===")
external_imgs = re.findall(r'https?://(?:www\.)?mounjax\.com[^\s"\'<>]+(?:webp|jpg|png|gif|svg|jpeg)', content)
for url in external_imgs:
    print(url)

print(f"\nTotal external mounjax.com images found: {len(external_imgs)}")
