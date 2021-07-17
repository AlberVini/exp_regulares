# greedy e non-greedy or lazy

import re 

texto = '''
<p>Something</p> <p>Qualquer coisa</p> <p>Frase 3 </p> <div>Frase 4 </div> 
'''

print(re.findall(r'<[pdiv]{1,3}>.+<\/[divp]{1,3}>', texto)) # greedy
print(re.findall(r'<[pdiv]{1,3}>.*?<\/[divp]{1,3}>', texto)[1]) # non-greedy
