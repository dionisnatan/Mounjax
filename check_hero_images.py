import re

with open('index.html', 'r', encoding='utf-8', errors='replace') as f:
    content = f.read()

# Find the hero section - look for the container with the heading text
# and extract background image URLs
hero_match = re.search(r'Gotinhas que auxiliam.*?queima de gordura', content, re.DOTALL)
if hero_match:
    start = max(0, hero_match.start() - 2000)
    end = min(len(content), hero_match.end() + 500)
    snippet = content[start:end]
    
    # Find any background image references
    bg_urls = re.findall(r'url\(["\']?([^"\')\s]+)["\']?\)', snippet)
    srcset = re.findall(r'srcset=["\']([^"\']+)["\']', snippet)
    src = re.findall(r'src=["\']([^"\']+)["\']', snippet)
    
    print("BG URLs in hero area:")
    for u in bg_urls:
        print(" ", u)
    print("\nIMG SRC in hero area:")
    for s in src:
        print(" ", s)
    print("\nIMG SRCSET in hero area:")
    for ss in srcset:
        print(" ", ss)
    print("\nRAW SNIPPET (first 1500 chars):")
    print(snippet[:1500])
