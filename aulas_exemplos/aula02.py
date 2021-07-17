# Meta caracteres: . ^ $ * + ? { } [ ] \ | ( )
# | OU
# . representa qualquer caractere (com exceção da quebra de linha)
# [] conjunto de caracteres = exp: [a-v] , [0-8]
# {} quantidade de caracteres
# flags determinam regras para a consulta

import re 

texto = '''
    Lorem, ipsum dolor sit amet consectetur adipisicing elit. Nulla soluta libero
    modi ad autem eaque fuga rerum. Amet architecto consequuntur delectus, qui sunt
    facere tempore natus explicabo provident, praesentium ut! 07/09/2021
'''

print(re.findall(r'Amet|amet', texto))
print(re.findall(r'[a-zA-Z0-9]met', texto))
print(re.findall(r'a........o', texto))
print(re.findall(r'[0-9]{2}/[0-9]{2}/[0-9]{4}', texto))
print(re.findall(r'LOREM', texto, flags=re.IGNORECASE))
