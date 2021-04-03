
#this is a main class
class vehicle:
    def __init__(self,name):#sorasori kono valu dite hole ' __init__' use hoy
        self.vehicle_name = name
    def name(self):
        print(self.vehicle_name)
a = vehicle("tata")
a.name()

#####################
print("\npass valu\n")
class stu:
    pass
stu.name = 'mj'
stu.roll = 131446
stu.group = 'cmt-a'
print(stu.name,stu.roll,stu.group)
