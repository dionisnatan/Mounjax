
import re

def list_links():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    links = re.findall(r'href=["\']([^"\']+)["\']', content)
    for i, link in enumerate(links):
        print(f"{i+1}: {link}")

if __name__ == "__main__":
    list_links()
