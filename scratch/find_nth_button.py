
import re

def find_nth_button(n):
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    matches = list(re.finditer(r'<a[^>]+class="[^"]*elementor-button[^"]*"[^>]+href="([^"]+)"', content))
    if len(matches) >= n:
        match = matches[n-1]
        start = max(0, match.start() - 500)
        end = min(len(content), match.end() + 500)
        print(f"--- Button {n} at {match.start()} ---")
        print(content[start:end])
        print("-" * 30)
    else:
        print(f"Only {len(matches)} buttons found.")

if __name__ == "__main__":
    import sys
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 12
    find_nth_button(n)
