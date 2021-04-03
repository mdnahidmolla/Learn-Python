# 0,1,1,2,3,5,8,13,21................n
def fibo(n):
    f = 0
    s = 1
    fibo = 1
    print(f)
    print(s)

    i = 3
    while i<=n:
        fibo = f+s
        print(fibo)
        f = s
        s = fibo
        i = i+1
n = int(input())
fibo(n)

