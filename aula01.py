import re

frase = 'Exemplo de expressão regular'

re.compile(frase)
print(re.findall(r'de', frase))
