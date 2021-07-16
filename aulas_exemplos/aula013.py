import re

cpf = '474.299.698-44'

print(re.findall(r'^[+-]?\d+', cpf))
