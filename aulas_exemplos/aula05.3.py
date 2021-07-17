# conjuntos () são alocados na memória, sendo assim, pode ser acessados e reutilizados
# () \1
# () () \1 \2
# (()) () \1 \2 \3
# para identificar cada grupo se conta a primera abertura de parênteses (
# para usar um conjunto mas não salva-lo na mémoria, se utiliza o "?:"" no começo do ()

import re 

cpf = '331.702.907-36'

print(re.findall(r'[0-9]{3}\.[0-9]{3}\.[0-9]{3}-[0-9]{2}', cpf)) # forma tradicional
print(re.findall(r'((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', cpf)) # com grupos
