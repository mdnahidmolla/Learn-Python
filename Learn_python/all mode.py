#mode ='w','b','r','x'
#plus|| text and bainary
#+ mean write and read


f = open('all mode.text','r+')
print(f.readable())
print(f.writable())
f.close()
#bainary
f = open('mjpic.jpg','rb')
print(f.read())
f.close()
