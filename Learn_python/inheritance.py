#inharitance holo duiti class er maje relationship kore
class vehicle:
    def __init__(self,name):#sorasori kono valu dite hole ' __init__' use hoy
        self.vehicle_name = name
    def name(self):
        print(self.vehicle_name)

class car(vehicle):
    def drive(self):
        print(self.vehicle_name,"is drive")
class truck(vehicle):
    def wheel(self):
        print(self.vehicle_name,"has 12 wheel")

#fancution call
a = car("tata")
a.name()
a.drive()
b = truck("toyeta")

b.wheel()
