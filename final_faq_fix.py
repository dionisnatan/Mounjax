import re
import os

def final_faq_fix():
    file_path = 'index.html'
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remove any 'open' attribute from details tags
    content = re.sub(r'<details\s+open', '<details', content)

    # 2. Update the script to handle BOTH opening and closing
    # and stop any other events
    pattern = r'<script>document\.addEventListener.*?<\/script>'
    
    new_script = """<script>
document.addEventListener('click', function(e) {
    var summary = e.target.closest('summary');
    if (summary) {
        e.preventDefault();
        e.stopPropagation();
        var details = summary.parentElement;
        if (details.hasAttribute('open')) {
            details.removeAttribute('open');
        } else {
            // Fecha outros se quiser (opcional), mas vamos focar em abrir este
            details.setAttribute('open', '');
        }
    }
}, true);
</script>"""

    content = re.sub(pattern, new_script, content, flags=re.DOTALL)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content if 'new_content' in locals() else content)
    
    print("FAQ Final Fix applied")

if __name__ == "__main__":
    final_faq_fix()
