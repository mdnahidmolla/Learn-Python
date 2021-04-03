
class Student:
    versity = "harverd univerchity"
    def __init__(self,student,subject,sec):
        self.student = student
        self.subject = subject
        self.sec = sec
    def show(self):
        print("\nstudent :",self.student,"\nsubject :",self.subject,"\nsec :",self.sec,"\nversity :",self.versity)
t = int(input("test case :"))
for i in range(1,t+1):
    n = Student(input("Enter student name : "),input("Enter subject name : "),input("Enter sec name : "))

n.show()


