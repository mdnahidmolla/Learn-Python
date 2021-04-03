#regular expresion
import re
a = 'My name is Nahid and i an a student'

#re.search(pattern,srting,flags<optional>)

#(.*----.*)
#. mean match any char
#* means zero or more num
#flags = re.I means case insensitive

b = re.search('.*and.*',a,re.I)
if b:
    print("true")

else:
    print("false")

print('\n')
c = 'Hello you are a Rohim and what Is Your Village Name'
d = re.search('(.*)and (.*)',c)
print(d.group(),)
print(d.group(1).capitalize(),' : ',d.group(1).upper())
print(d.group(2),' : ',d.group(2).lower())

