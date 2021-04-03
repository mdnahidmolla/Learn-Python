# non local is not golabal and local
def a():
    x = 3
    def f():

        nonlocal x
        x = 4
    f()
    print(x)
a()
