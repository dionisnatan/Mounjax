import re

with open('index.html', 'r', encoding='utf-8', errors='replace') as f:
    content = f.read()

# Find the hero section container - it's an e-lazyloaded container
# The hero is the first major section. Let's look at the first container's background
# Look for background image set by Elementor in the data-settings attribute
data_settings = re.findall(r'data-settings="({[^"]+})"', content[:15000])
print(f"data-settings found in first 15000 chars: {len(data_settings)}")
for ds in data_settings[:5]:
    print(ds[:300])
    print("---")

# Also look for background image in style attributes near the hero
styles_with_bg = re.finditer(r'style="([^"]*background[^"]*)"', content[:15000])
for m in styles_with_bg:
    print("INLINE STYLE:", m.group(1)[:300])
    print("---")

# Look for lazyloaded elements
lazy_match = re.findall(r'e-lazyloaded[^>]*data-settings=.{0,500}', content[:15000])
for lm in lazy_match:
    print("LAZY:", lm[:500])
    print("---")
