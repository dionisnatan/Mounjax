import re

with open('index.html', 'r', encoding='utf-8', errors='replace') as f:
    content = f.read()

# Look for CSS in the <style> tag and find all background-image URLs there
style_blocks = re.findall(r'<style[^>]*>(.*?)<\/style>', content, re.DOTALL)
print(f"Found {len(style_blocks)} style blocks")

for i, block in enumerate(style_blocks):
    bg_urls = re.findall(r'url\(["\']?([^"\')\s]+)["\']?\)', block)
    if bg_urls:
        print(f"\n=== Style block {i+1} background URLs ===")
        for url in bg_urls:
            print(f"  {url}")

# Also check CSS files for background images pointing to mounjax.com
import os
css_files = [f for f in os.listdir('css') if f.endswith('.css')]
print(f"\n\nChecking {len(css_files)} CSS files for external image URLs...")
for cf in css_files[:5]:
    with open(f'css/{cf}', 'r', encoding='utf-8', errors='replace') as f:
        css_content = f.read()
    external_bg = re.findall(r'url\(["\']?(https?://[^"\')\s]+)["\']?\)', css_content)
    if external_bg:
        print(f"\n{cf}:")
        for url in external_bg[:10]:
            print(f"  {url}")
