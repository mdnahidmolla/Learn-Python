#magic method
class stu:
    def __init__(self,name,roll):
        self.name = name
        self.roll = roll
    def __repr__(self): #repr use korle fancation coll diya lage na #sora sori man print kora jai
        return self.name,self.roll
    def __str__(self):
        return self.name
a = stu("mj",131446)
print(a.__repr__())
print(a.__str__())
