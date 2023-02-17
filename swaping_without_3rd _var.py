import math
a=int(input("Enter a number"))
b=int(input("Enter another number"))
print("The values of variables before swaping"+"\na="+str(a)+"and b="+str(b)+"\n")
a=a*(pow(10,len(str(b))))
a=a+b
b=int(a/(pow(10,len(str(b)))))
a=str(a%(pow(10,len(str(b)))))
print("The vale of a and b after swaping "+"\na="+a+"and b="+str(b))