
import os
import re

def check_images():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all src="..." and srcset="..." references to images/
    srcs = re.findall(r'src=["\'](images/[^"\']+)["\']', content)
    srcsets = re.findall(r'srcset=["\']([^"\']+)["\']', content)
    
    all_refs = set(srcs)
    for sset in srcsets:
        # srcset can have multiple comma separated paths with sizes
        parts = sset.split(',')
        for part in parts:
            match = re.search(r'(images/[^ ]+)', part.strip())
            if match:
                all_refs.add(match.group(1))
    
    missing = []
    for ref in all_refs:
        if not os.path.exists(ref):
            missing.append(ref)
            
    if missing:
        print("Missing images:")
        for m in missing:
            print(f"- {m}")
    else:
        print("All image references are present in the images/ folder.")

if __name__ == "__main__":
    check_images()
