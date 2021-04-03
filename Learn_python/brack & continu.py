#continu mean = skip
i = 1
while i<=10:
    if i==5:
        i=i+1
        continue

    print(i)
    i = i+1

print("\t")
#break mean = stop
for i in range(1,10):
    if i == 5:
        break
    print(i)
