import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8', errors='replace') as f:
    content = f.read()

original_len = len(content)

# Find all escaped mounjax.com URLs
escaped_urls = re.findall(r'https?:\\/\\/mounjax\.com[^\s"\'<>]+(?:webp|jpg|png|gif|svg|jpeg)', content)
unique_escaped = list(dict.fromkeys(escaped_urls))

print("Found escaped URLs:")
for u in unique_escaped:
    print(u)

# Let's just do a mass replace for the specific images we know are failing
replacements = {
    r'https?:\\/\\/mounjax\.com\\/wp-content\\/uploads\\/2025\\/06\\/banner1\.webp': 'images/banner1.webp',
    r'https?:\\/\\/mounjax\.com\\/wp-content\\/uploads\\/2025\\/06\\/cropped-cone_monjax_1\.webp': 'images/cropped-cropped-cone_monjax_1-180x180.webp',
    r'https?:\\/\\/mounjax\.com\\/wp-content\\/uploads\\/2025\\/06\\/cropped-cropped-cone_monjax_1-270x270\.webp': 'images/cropped-cropped-cone_monjax_1-180x180.webp'
}

for pattern, replacement in replacements.items():
    content = re.sub(pattern, replacement, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Fixed escaped URLs! File size: {original_len} -> {len(content)}")
