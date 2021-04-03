#regular expresion -match

import re
a = 'my name is mj and he is a student'
#re.match(pattren,str,flags<>)
p = re.match('my.*',a)
if p:
    print('match')
else:
    print('not match')
print('\n')

p = re.match('(my.*)and (.*student)',a)
print(p.group(1))
print(p.group(2))
