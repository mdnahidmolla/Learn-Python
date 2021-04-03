
from datetime import date

class Exe:
    def __init__(self,per1,per2):
        self.per1 = per1
        self.per2 = per1

    @classmethod
    def dathbirth(cls,per1,per2):
        return cls(date.today().year - per1,date.today().year - per2)

    @staticmethod
    def age(per1,per2):
        return (per1,per2)

a = Exe(2000,1996)
Exe.age()



