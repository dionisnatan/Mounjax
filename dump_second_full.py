import re

with open('index.html', 'r', encoding='utf-8', errors='replace') as f:
    content = f.read()

match = re.search(r'<details id="e-n-accordion-item-3171".*?<\/details>', content, re.DOTALL)
if match:
    print("SECOND BLOCK CONTENT:")
    print(match.group(0))
