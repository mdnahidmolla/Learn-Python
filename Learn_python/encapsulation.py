#encapsulation - > data ->*public **protected ***privet
class Name:
    def __init__(self,name):
        self.name = name #public
        self._name = name #protected
        self.__name = name

a = Name("nahid")
print("public :",a.name)
print("protected :",a._name)
print("private :",a._Name__name)
