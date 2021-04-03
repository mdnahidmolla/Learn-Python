#try:
    #main code
#except divisionerror:
#many except hole(nameerror,typerror)

#zero division error
try:
    a = 0
    print(10/a)
except ZeroDivisionError:
    print("zero division error")

#Name error
try:
    print(10/a)
except NameError:
    print("Name error")

#type error

try:
    print(10/'5')
except TypeError:
    print("Type error")

