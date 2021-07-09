# Meta caracteres: . ^ $ * + ? { }  \  ( )
# a regra dos meta caracteres se aplica sempre ao crct a esquerda
# * 0 ou n
# + 1 ou n
# ? 0 ou 1
# {n} quantidade de caracteres
# {min, max}

import re

texto = '''
João trouxe flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.
Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm"!
'''

print(re.findall(r'vi*da', texto, flags=re.I)) # exemplo linha 3
print(re.findall(r'jo+ão', texto, flags=re.I)) # exemplo linha 4
print(re.findall(r'jo?ão', texto, flags=re.I)) # exemplo linha 5
print(re.findall(r'j[a-z]+ão', texto, flags=re.I)) # pode ser usado em um conjunto
print(re.findall(r've{3}m{1,4}', texto, flags=re.I)) # exemplo linha 7
print(re.sub(r'jo+ão+', 'Vinicius', texto, flags=re.I)) # simples substituição

texto2 = 'Felipe ama ser amado'

print(re.findall(r'ama[do]*', texto2, flags=re.I))
# print(re.findall(r'ama[od]{0,2}', texto2))
