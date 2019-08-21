import time,random

timesleep =600

print("Hello,World")
x,y,z ='Rakan' ,'Eid' ,'Almutairi'
print("\n",x,y,z)

#random number
a =random.randrange(0,10)
print("\nRandom number range 0-10 =>",a)

#varibales and changes type
x1 =10
x2 =10.15
x3 =10j
print("\n\tx1",x1,type(x1),"\n\tx2",x2,type(x2),"\n\tx3",x3,type(x3),"\nChange type")
x1=float(x1)
x2=int(x2)
print("\tx1",x1,type(x1),"\n\tx2",x2,type(x2),"\n\tx3",x3,type(x3),"====>Can't change the type xD")
print("\nsleep time",timesleep)
time.sleep(timesleep) #pasue to 600 sec 