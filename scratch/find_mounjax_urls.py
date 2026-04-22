
import re

def find_mounjax_urls():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Simple regex to find URLs starting with https://mounjax.com
    urls = re.findall(r'https?://mounjax.com/[^\s\"\'>\\]+', content)
    # Also handle escaped slashes in JSON
    urls_escaped = re.findall(r'https?://mounjax.com/(?:[^\s\"\'>\\]|\\/)+', content)
    
    all_urls = set(urls) | set(urls_escaped)
    
    if all_urls:
        print("Found URLs pointing to mounjax.com:")
        for url in sorted(all_urls):
            print(f"- {url}")
    else:
        print("No URLs pointing to mounjax.com found.")

if __name__ == "__main__":
    find_mounjax_urls()
