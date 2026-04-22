import re
import os

def fix_toggle_script():
    file_path = 'index.html'
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the existing script I added
    pattern = r'<script>document\.addEventListener.*?<\/script>'
    
    new_script = """<script>
document.addEventListener('click', function(e) {
    var summary = e.target.closest('summary');
    if (summary) {
        var details = summary.parentElement;
        // Se já estiver aberto, remove o atributo 'open' para fechar
        if (details.hasAttribute('open')) {
            e.preventDefault();
            e.stopPropagation();
            details.removeAttribute('open');
        }
    }
}, true); // Use capture phase to run before Elementor
</script>"""

    new_content = re.sub(pattern, new_script, content, flags=re.DOTALL)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print("Toggle script updated successfully")

if __name__ == "__main__":
    fix_toggle_script()
