import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'<details id="e-n-accordion-item-3170".*?</details>', content, re.DOTALL)
if match:
    print("MATCH FOUND:")
    print(match.group(0))
else:
    print("NOT FOUND")
