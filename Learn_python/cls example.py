class tai:
    def __init__(self,height,width):
        self.height = height
        self.width = width
    def area(self):
        print(self.height * self.width)
    @classmethod
    def sq(cls,num):
        return cls(num,num)
a = tai(4,5)
a.area()
b = tai.sq(4)
b.area()
