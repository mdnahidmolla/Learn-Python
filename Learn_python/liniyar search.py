def linear_search(l,x): #l = list
    n = len(l)
    i=0
    for i in range(n):
        if l[i]==x:
            return i
        return -1

