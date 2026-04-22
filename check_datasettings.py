import re
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8', errors='replace') as f:
    content = f.read()

# Elementor sets background images via data-settings JSON attribute
# Find all data-settings that contain image/url references
settings_pattern = re.compile(r'data-settings="([^"]+)"')

print("=== ALL data-settings with image/background URLs ===")
for m in settings_pattern.finditer(content):
    raw = m.group(1)
    if 'url' in raw.lower() or 'image' in raw.lower():
        # Unescape HTML entities
        raw = raw.replace('&quot;', '"').replace('&#34;', '"').replace('&amp;', '&')
        print(raw[:600])
        print("---")
