class Stu():
    clz = "mangrove institute"
    def __init__(self,stu,roll,sec):
        self.stu = stu
        self.roll = roll
        self.sec = sec
    def show(self): #instance method kaj kore object niye = self.
        print(self.stu,self.roll,self.sec)
    @classmethod #akta fancation use kore onno akta funcation make kora
    def seen(cls): #class method kaj kore class niye = cls.
        print(cls.clz)
d = Stu("mj",131446,"a")
d.show()
d.seen()


