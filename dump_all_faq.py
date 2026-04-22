import re

with open('index.html', 'r', encoding='utf-8', errors='replace') as f:
    content = f.read()

details_blocks = re.findall(r'<details.*?</details>', content, re.DOTALL)
print(f"Found {len(details_blocks)} details blocks")

if len(details_blocks) >= 2:
    print("FIRST BLOCK:")
    print(details_blocks[0][:400])
    print("\nSECOND BLOCK:")
    print(details_blocks[1][:400])
