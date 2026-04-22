
import re

def list_button_links():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Match elementor buttons
    buttons = re.findall(r'<a[^>]+class="[^"]*elementor-button[^"]*"[^>]+href="([^"]+)"', content)
    
    for i, href in enumerate(buttons):
        print(f"Button {i+1}: {href}")

if __name__ == "__main__":
    list_button_links()
