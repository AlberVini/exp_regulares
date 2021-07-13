# código versão reduzida da aula09
import re

ip_reg_exp = re.compile(r'^(?:(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]\d|\d)\.?){4}\b$')

# ip de 0.0.0.0 ~ 299.299.299.299
for i in range(300):
    ip = f'{i}.{i}.{i}.{i}'
    if len(ip_reg_exp.findall(ip)) > 0:
        print(f'{ip_reg_exp.findall(ip)} é válido')
    else:
        print(f'{ip} é inválido')
