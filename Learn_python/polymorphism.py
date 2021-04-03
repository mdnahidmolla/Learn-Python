#polymorphison ->may forms
# akta jinishe onake bebohar

class man:
    def name(self):
        print("nahid +")
                            # name = name two bebohar
class man2:
    def name(self):
        print("+suma")
a = man()
b = man2()

for obj in (a,b):
    obj.name()
