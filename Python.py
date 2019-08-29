import time,random

timesleep =600
#random 
def FirstWeek():
    print("#####First Week #######\n")
    a =random.randrange(0,10)
    print("Random number range 0-10 =>",a)
    #varibales and changes type
    x1 =10
    x2 =10.15
    x3 =10j
    print("\n\tx1",x1,type(x1),"\n\tx2",x2,type(x2),"\n\tx3",x3,type(x3),"\nChange type")
    x1=float(x1)
    x2=int(x2)
    print("\tx1",x1,type(x1),"\n\tx2",x2,type(x2),"\n\tx3",x3,type(x3),"====>Can't change the type xD")
def SecoundWeek():
    print("##### SecoundWeek ###### \n")
    a ='''Hello,World
    this is a practise for python'''
    #string practise 
    print(a) #print multi line 
    a="Hello,World"
    print(a[11:41]) #print range from 11 to 41 
    print(a.strip()) #eraise whitespace in start of string
    print(len(a)) #print length of the string
    print(a.upper(),"\t",a.lower()) #uppper alph ,lower
    print(a.replace("Hello,World","Hi there")) #replce 
    print(a.split(',')) #split by ","
    a="Hello,World {}"
    x=20
    print(a.format(x)) #replace {} by x 
    a="Hello{0}World\t{1}"
    print(a.format(',',20)) #multi replace format
def Oprations():
    x,y =3,12
    a=["Rakan","Khaled"]
    print(x is not y)
    print(x // y)
    print("Rakan" in a) #search Rakan is it in a list

#lessons fun 
#FirstWeek()
SecoundWeek()
#Oprations()