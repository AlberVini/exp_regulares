# conjuntos () são alocados na memória, sendo assim, pode ser acessados e reutilizados
# () \1
# () () \1 \2
# (()) () \1 \2 \3
# para identificar cada grupo se conta a primera abertura de parênteses (
# para usar um conjunto mas não salva-lo na mémoria, se utiliza o "?:"" no começo do ()

import re

texto_html = '<p>1° Parágrafo</p> <p>2° Parágrafo</p> <div>Exemplo div</div>'

# nomeação de conjunto (somente em python)
# usasse (?P<exemplo>...) e para o acesso (?P=exemplo)
# print(re.findall(r'<(?P<ptag>[pdiv]{1,3})>(.+?)<\/(?P=ptag)>', texto_html))

print(re.sub(r'(<(.+?)>)(.+?)(<\/\2>)', r'\1"\3"\4', texto_html))
