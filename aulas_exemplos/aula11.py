import re 

num_telef = '''
(21) 9 4567-5345
(11)9 8735-6697
(45) 94508-7096
(91) 9408-8296
(65)    9 4568-7896
9 4687-4567
1234-5437
'''

num_telef_regex = re.findall(r'^\(\d{2}\)\s*9{1}\s*\d{4}-\d{4}$', num_telef, flags=re.M)

print('Números autenticados: ')
for num_auth in num_telef_regex:
    print(num_auth, end=' ')
