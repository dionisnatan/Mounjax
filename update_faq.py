import re
import os

def update_faq():
    file_path = 'index.html'
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern for the first FAQ item answer
    # data-id="d69e910"
    pattern = r'(data-id="d69e910".*?elementor-heading-title elementor-size-default">)(.*?)(</h2>)'
    
    new_text = "Mounjax está alinhado com as normas da ANVISA para comercialização e sem nenhuma restrição pelo órgão.<br><br>Por se tratar de um Suplemento alimentar seguro para consumo, Mounjax é um produto dispensado da obrigatoriedade de registro."
    
    def replacement(match):
        return match.group(1) + new_text + match.group(3)

    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print("FAQ updated successfully")

if __name__ == "__main__":
    update_faq()
