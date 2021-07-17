# https://regex101.com/r/W4kRV2/2/
# https://en.wikipedia.org/wiki/List_of_Unicode_characters
import re
from aula012 import lista_senhas

senha_forte_regexp = re.compile(
    r'^'
    r'(?=.*[a-z])'
    r'(?=.*[A-Z])'
    r'(?=.*[0-9])'
    r'(?=.*[ -\/:-@[-`{-~])'
    r'.{12,}'
    r'$',
    flags=re.M
)

strings = lista_senhas()

print('Senhas válidas ou fortes')
for senha in strings:
    if senha_forte_regexp.search(senha):
        print(senha_forte_regexp.findall(senha))
