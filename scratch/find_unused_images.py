
import os
import re

def find_unused_images():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Also check CSS files
    css_files = [f for f in os.listdir('css') if f.endswith('.css')]
    for css_file in css_files:
        with open(os.path.join('css', css_file), 'r', encoding='utf-8') as f:
            content += f.read()
            
    all_images = os.listdir('images')
    unused = []
    for img in all_images:
        if img not in content:
            unused.append(img)
            
    if unused:
        print("Unused images in images/ folder:")
        for img in unused:
            print(f"- {img}")
    else:
        print("All images in images/ folder are referenced in HTML or CSS.")

if __name__ == "__main__":
    find_unused_images()
