import re

exemplos = '''
Válidos
0.0
00.00
000.000
+0.0
-00.00
+000.000
10
50
8.5
-8.5
+10.5005412136
1231345458.54654564
-133215646589.6543215648978977
+1.11123123
-0.154987
1.121654987
10.123
10.1
-1.1
Inválidos
10..2
++1213
--1235050
.124546
-.1231324
10.
.1
.10
10.
+10.
-10.
5a
b5
'''

def is_float(number):
    return bool(re.search(r'^[+-]?\d+(?:\.\d+)?$', number))


def is_int(number):
    return bool(re.search(r'^[+-]?\d+$', number))


while True:
    n1 = input('Digite um número | [S] para sair: ')
    if n1 == 'S':
        break
    else:
        if is_int(n1):
            numero = int(n1)
            print(f'O número {numero} é do tipo inteiro')
            continue

        if is_float(n1):
            numero = float(n1)
            print(f'O número {numero} é do tipo float')
            continue

        if type(n1) == str:
            print(f'{n1} é um número inválido ou do tipo string')
