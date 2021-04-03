#reduction --> reduce
#reduce =  bainary_funcation,sequence

from functools import reduce
def func(x,y):
    return x*y
a = [1,2,3,4,5,6]
b = reduce(func,a)
print(b)

