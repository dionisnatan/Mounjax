import re

with open('index.html', 'r', encoding='utf-8', errors='replace') as f:
    content = f.read()

# Find the second FAQ item by searching for "contraindica"
match = re.search(r'<details id="e-n-accordion-item-[0-9]+".*?contraindica.*?<\/details>', content, re.DOTALL)
if match:
    print("MATCH FOUND:")
    print(match.group(0)[:800])
else:
    print("NOT FOUND")
