
class a():
    def __init__(self,name,color):
        self.name = name
        self.color = color
    def Name(self):
        print(self.name)

    def info(self):
        print(self.color)
class b(a):
    def info(self):
        print("bad")
c = b("mj","good")
c.Name()
c.info()
