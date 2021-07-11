# ^ a expressão deve começar de x maneira
# ^ [^a-z] serve para negar algo em especifico
# $ a expressão deve terminar de x maneira
# os meta caracteres acima servem para a busca exata da expressão passada

import re

cpf = '293.457.246-99'
cpf2 = 'a 293.457.246-99'

print(re.findall(r'^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})$', cpf))
print(re.findall(r'^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})$', cpf2))

print(re.findall(r'[^a-z]+', cpf2))
