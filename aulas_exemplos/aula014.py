import re

emails = '''
example@s.example.br
a@a.com.br
mailhost!username@example.org
user%example.com@example.org
email@example.com
'''

regex = re.compile(r'^\w+(?:[.\-+!%]\w+)*@\w+(?:[.\-]\w+)+$', flags=re.M)

print(regex.findall(emails))
