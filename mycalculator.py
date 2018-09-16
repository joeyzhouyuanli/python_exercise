print('My calculator')
#define the functions
def add(x,y):
 return x+y
def minus(x,y):
 return x-y
def multiply(x,y):
 return x*y
def divide(x,y):
  return x/y 

 #input by user
print("What you want to do")
print("1=add")
print("2=minus")
print("3=multiply")
print("4=divide")

choice=input("please type 1~4\n")
a=float(input("a="))
b=float(input("b="))

if choice=='1':
    print(a,"+",b,"=",add(a,b))
elif choice=='2':
    print(a,"-",b,"=",minus(a,b))
elif choice=='3':
    print(a,"*",b,"=",multiply(a,b))
elif choice=='2':
    print(a,"/",b,"=",divide(a,b))
else:
	print("invalid input")