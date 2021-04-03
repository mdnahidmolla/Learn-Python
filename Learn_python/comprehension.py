#list comprehension
# a  = {x!x E N and 1<=x<=5}
a = [x for x in range(1,6)]
print(a)
# a  = {x!x E N and x is even number 1<=x<=10}
a = [x for x in range(1,10)if x%2==0]
print(a)
# a  = {x!x E N and x**2 and  1<=x<=10}
a = [x**2 for x in range(1,6)]
print(a)
