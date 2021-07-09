import re

frase = 'Exemplo de expressão regular'

print(re.search(r'expressão', frase))
print(re.findall(r'expressão', frase))
print(re.sub(r'expressão', 'exp', frase))

fixo = re.compile(r'Exemplo') # guardando em uma variável a procura
# manipulação da variável
print(fixo.search(frase))
print(fixo.findall(frase))
print(fixo.sub('Exp', frase))
