import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Check the post-2108.css file which contains per-page Elementor styles
with open('css/post-2108.css', 'r', encoding='utf-8', errors='replace') as f:
    css = f.read()

# Find background-image rules with URLs (not just gradients)
url_bg_rules = re.findall(r'[^{]+\{[^}]*background-image\s*:\s*url\([^)]+\)[^}]*\}', css)
print(f"Found {len(url_bg_rules)} background-image URL rules")
for rule in url_bg_rules[:20]:
    print("\n" + rule[:500])
    print("---")

# Also find ALL url() references 
all_urls = re.findall(r'url\(["\']?([^"\')\s]+)["\']?\)', css)
print("\n\n=== All URLs in post-2108.css ===")
for url in all_urls:
    print(url)
