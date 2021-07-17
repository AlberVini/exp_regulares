# validador de ip e cpf

import re

# cpf
cpf = input('Digite um cpf com o formato [XXX.XXX.XXX-XX]: ')
cpf_reg_exp = re.compile(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$')

if cpf_reg_exp.search(cpf):
    print(f'{cpf} válido')
else:
    print('Digite um cpf válido')

# ip
# versão explicada
ip_reg_exp = re.compile(r'''
    ^
    (?:
        (?:
            25[0-5]| # 250 - 255
            2[0-4]\d| # 200 - 249
            1\d{2}| # 100 - 199
            [1-9]\d| # 10 - 99
            \d # 0 - 9
        )
        \.
    ){3}
        (?:
            25[0-5]| # 250 - 255
            2[0-4]\d| # 200 - 249
            1\d{2}| # 100 - 199
            [1-9]\d| # 10 - 99
            \d # 0 - 9
        )
    $
''', flags=re.VERBOSE) # a flag re.VERBOSE ou re.X permite comentários por exemplo no código


# ip de 0.0.0.0 ~ 299.299.299.299
for i in range(300):
    ip = f'{i}.{i}.{i}.{i}'
    if len(ip_reg_exp.findall(ip)) > 0:
        print(f'{ip_reg_exp.findall(ip)} é válido')
    else:
        print(f'{ip} é inválido')
