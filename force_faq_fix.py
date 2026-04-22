import re

def fix_faq():
    file_path = 'index.html'
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remove ANY 'open' attribute from details (open="" or just open)
    content = re.sub(r'<details([^>]*)open(?:=""|)', r'<details\1', content)
    
    # 2. Add inline onclick to summary to FORCE bypass Elementor
    # Find summary tags and add the onclick attribute
    onclick_code = 'onclick="event.preventDefault(); event.stopPropagation(); this.parentElement.toggleAttribute(\'open\');"'
    
    # Only add it if not already there
    def add_onclick(match):
        tag_content = match.group(0)
        if 'onclick=' not in tag_content:
            return tag_content.replace('<summary', f'<summary {onclick_code}')
        return tag_content

    content = re.sub(r'<summary.*?>', add_onclick, content)

    # 3. Clean up the previous script block we added to avoid conflicts
    content = re.sub(r'<script>\s*document\.addEventListener\(\'click\'.*?<\/script>', '', content, flags=re.DOTALL)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("FAQ Inline Fix Applied")

if __name__ == "__main__":
    fix_faq()
