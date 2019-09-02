print("##### SecoundWeek ###### \n")
a ='''Hello,World
this is a practise for python'''
#string practise 
print(a) #print multi line 
a="Hello,World"
print(a[1:4]+"\t#print range from 1 to 4") 
print(a.strip()+"\t#eraise whitespace in start of string")
print(len(a),"\t#print length of the string") 
print(a.upper(),"\t",a.lower()+"\t#uppper alph ,lower") 
print(a.replace("Hello,World","Hi there")+"\t#replce") 
print(a.split(','),"#\tsplit by ','") 
a="Hello,World {}"
x=20
print(a.format(x)+"\t#replace {} by x")  
a="Hello{0}World\t{1}"
print(a.format(',',20)+"\t#multi replace format")
x,y =3,12
a=["Rakan","Khaled"]
print(x is not y)
print(x // y)
print("Rakan" in a,"\t#search Rakan is it in a list")