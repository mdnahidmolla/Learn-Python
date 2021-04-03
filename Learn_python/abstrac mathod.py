from abc import ABC,abstractclassmethod

class father(ABC): # prents class dorker but kono object dorker na tahole ai method use hoy
    def study(self):
        pass

class son(father):
    def __init__(self,name):
        self.name  = name

    def show(self):
        print(self.name)

    def study(self):
        print("yes.father")

a = son("mj")
a.show()
a.study()
