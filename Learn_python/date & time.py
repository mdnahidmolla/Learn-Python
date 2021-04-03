import datetime
time = datetime.time(20,10,23)#hour,min,sec
print("hour :",time.hour)
print('min :',time.minute)
print('sec :',time.second)

print('time \n')
time1 = datetime.datetime.now()
print('hour :',time1.hour)
print('min :',time1.minute)
print('sec :',time1.second)


print("date \n")
print(datetime.date.today())

print('imoprt date \n')
from datetime import date
print(date.today())



'''dete = datetime.date(2019,3,19)
print('year :',date.year)
print('month :',date.month)
print('day :',date.day)'''
