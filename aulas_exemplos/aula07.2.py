# flags
# re.I | re.IGNORECASE
# re.A | re.ASCII tabela ASCII
# re.M | re.MULTILINE -> auxilia na utilização do ^$ em uma expressão
# re.S | re.DOTALL 

import re

texto = '''
123.435.764-77 ABC
197.744.069-99
777.444.222.00 DEF
'''
print(re.findall(r'^\d{3}.\d{3}.\d{3}-\d{2}$', texto, flags=re.M))

texto2 = 'Tuplas são imutáveis, se quiser \n um tipo de conjunto mutavel, utilize listas'

print(re.findall(r'^t.*s$', texto2, flags=re.I | re.S))
