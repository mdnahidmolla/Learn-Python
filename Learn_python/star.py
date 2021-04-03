n = 5#int(input("enter a  valu : "))
'''
for i in range(1,n+1):#line colom
    for j in range(1,i+1):#shari
        print("* ",end="")
    print()
'''
for i in range(n,0,-1):
    for j in range(0,i):
        print("* ",end=" ")
    print()
