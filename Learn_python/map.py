def ha(x):
    return x**2
a = [1,2,3,4,5]
b = list(map(ha,a))
c = list(map(lambda x : x+1,b))

print(b)
print(c)
