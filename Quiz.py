def Quize1():
    x,y,z="apple","orange","limon"
    basket = x +' '+ y+' '+ z
    print(basket)
def Quize2():
    a="Please,I want {} sandwitches and {} donutes"
    a=a.replace('I','We')
    a=a.format(5,7)
    a=a.replace('a','A')
    print(a)
print("######Quiz 01#####")
Quize1()
print("######Quiz 02#####")
Quize2()