def avarage(l):
    if not l:
        return None
    return sum(l)/len(l)
if __name__ =="__main__":  #ans na jana thikle ai tha use korbo
    l = [1,2,3,4,5]
    print(avarage(l))
