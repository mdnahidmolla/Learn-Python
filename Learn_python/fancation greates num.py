def greats(a,b,c):
    if a>b:
        if a>c:
            print(a,"a is the greates number")
    elif b>a:
        if b>c:
            print(b,"b is the greates number")
    else:
        print(c,"c  is the greates number")
a = int(input())
b = int(input())
c = int(input())
print(greats(a,b,c))
