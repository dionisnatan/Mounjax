import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8', errors='replace') as f:
    content = f.read()

# Elementor also stores settings inside the inline JS object
# Look for elementorFrontendConfig or similar
js_settings = re.search(r'var elementorFrontendConfig\s*=\s*({.*?});', content, re.DOTALL)
if js_settings:
    print("Found elementorFrontendConfig:")
    print(js_settings.group(1)[:2000])
else:
    print("elementorFrontendConfig not found")

# Check for any CSS rules setting background-image for hero containers
print("\n=== CSS style blocks - background-image rules ===")
style_blocks = re.findall(r'<style[^>]*>(.*?)<\/style>', content, re.DOTALL)
for i, block in enumerate(style_blocks):
    if 'background-image' in block:
        lines = [l.strip() for l in block.split('\n') if 'background-image' in l]
        print(f"Style block {i+1}:")
        for line in lines:
            print(f"  {line[:300]}")

# Check the post CSS file which Elementor generates per-page with background images
import os
css_dir = 'css'
for cf in os.listdir(css_dir):
    filepath = os.path.join(css_dir, cf)
    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        css = f.read()
    if 'background-image' in css:
        print(f"\n{cf} has background-image rules:")
        lines = [l.strip() for l in css.split('\n') if 'background-image' in l]
        for line in lines[:20]:
            print(f"  {line[:300]}")
