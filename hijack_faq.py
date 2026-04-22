import re

def absolute_faq_fix():
    file_path = 'index.html'
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remove the old inline onclick we added to avoid conflicts
    content = re.sub(r' onclick="event\.preventDefault\(\); event\.stopPropagation\(\); this\.parentElement\.toggleAttribute\(\'open\'\);"', '', content)
    
    # 2. Make sure details starts closed
    content = re.sub(r'<details([^>]*)open(?:=""|)', r'<details\1', content)

    # 3. Inject our Hijack Script before the closing body tag
    hijack_script = """
<script>
// SCRIPT DEFINITIVO PARA O FAQ
document.addEventListener("DOMContentLoaded", function() {
    // Dá um tempo para o Elementor carregar os scripts dele
    setTimeout(function() {
        document.querySelectorAll("details.e-n-accordion-item").forEach(function(details) {
            var summary = details.querySelector("summary");
            if (!summary) return;
            
            // Clona o summary para arrancar TODOS os event listeners do Elementor!
            var newSummary = summary.cloneNode(true);
            summary.parentNode.replaceChild(newSummary, summary);
            
            // Garante que começa fechado
            details.removeAttribute("open");
            newSummary.setAttribute("aria-expanded", "false");
            
            // Adiciona nosso próprio evento, imune a erros
            newSummary.addEventListener("click", function(e) {
                e.preventDefault(); // Impede o navegador de bugar
                
                var isOpen = details.hasAttribute("open");
                
                // Fecha todos os outros primeiro
                document.querySelectorAll("details.e-n-accordion-item").forEach(function(d) {
                    d.removeAttribute("open");
                    var s = d.querySelector("summary");
                    if(s) s.setAttribute("aria-expanded", "false");
                    
                    // Limpa qualquer estilo de display:none que o Elementor possa ter deixado
                    var content = d.querySelector("div");
                    if(content) content.style.display = '';
                });
                
                // Se estava fechado, abre esse
                if (!isOpen) {
                    details.setAttribute("open", "");
                    newSummary.setAttribute("aria-expanded", "true");
                }
            });
        });
    }, 1000); // Executa 1 segundo após carregar a página para ter certeza que sobrescreve o Elementor
});
</script>
"""
    
    # Remove any previous hijack script we might have added (just in case)
    content = re.sub(r'<script>\s*// SCRIPT DEFINITIVO.*?<\/script>', '', content, flags=re.DOTALL)
    
    # Insert right before </body>
    if '</body>' in content:
        content = content.replace('</body>', hijack_script + '</body>')
    else:
        content += hijack_script

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("Definitive FAQ Hijack Script Applied")

if __name__ == "__main__":
    absolute_faq_fix()
