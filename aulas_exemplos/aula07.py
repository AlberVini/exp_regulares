# shorthand
# \w para encontrar -> [a-zA-Z0-9À-ú] 
# \W negação [^a-zA-Z0-9À-ú]
# \d para encontrar só números -> [0-9]
# \D negação [^0-9]
# \s [\r\n\f\t]
# \S negação, bom para eliminar espaços de strings
# \b borda, capta uma palavra com determinado começo ou final
# \b para encontrar uma palavra com determinado número de caracteres
# \B estranho mas tem a função de não encontrar uma borda

import re

texto = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.
Foi um ano excelente na vida de joão. Teve_ALGO 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm"!
'''

# print(re.findall(r'[a-zA-Z0-9À-ú]+', texto))
# print(re.findall(r'\w+', texto))

# print(re.findall(r'[0-9]+', texto))
print(re.findall(r'\d+', texto))

print(re.findall(r'\S+', texto))

print(re.findall(r'\bt\w+', texto, flags=re.I)) # begin
print(re.findall(r'\w+da\b', texto, flags=re.I)) # tail
print(re.findall(r'\b\w{7}\b', texto)) # linha 9
print(re.findall(r'atual\w{2}\B', texto))
