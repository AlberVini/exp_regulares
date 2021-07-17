# conjuntos () são alocados na memória, sendo assim, pode ser acessados e reutilizados
# () \1
# () () \1 \2
# (()) () \1 \2 \3
# para identificar cada grupo se conta a primera abertura de parênteses (

import re 

texto = '''
<p>Something</p> <p>Qualquer coisa</p> <p>Frase 3 </p> <div>Frase 4 </div> 
'''

tags = re.findall(r'(<([p|div]{1,3})>(.+?)<\/\2>)', texto)
tags2 = re.findall(r'<([p|div]{1,3})>(?:.+?)<\/\1>', texto) # nesse caso, o grupo com ?: não será salvo 

print(tags2)

for tag in tags:
    primeira_tag, fechamento_tag, conteudo_tag, = tag
    print(conteudo_tag)
