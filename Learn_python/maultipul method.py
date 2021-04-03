from datetime import date

class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    @classmethod
    def birthdate(cls,name,year):
        return cls(name,date.today().year - year)

    @staticmethod
    def adult(age):
        return age>18

a = person("mj",2000)
print("name :",a.name,"\nage :",a.age,"adult-->",person.adult(a.age))
