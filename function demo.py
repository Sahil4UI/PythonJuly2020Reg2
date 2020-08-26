#User Defined Functions

#Function Definition
#type-1 Default function -without arguement without return type
def add():
    a = int(input("Enter Number 1: "))
    b = int(input("Enter Number 2: "))
    print(a+b)

#Function Calling
#add()
#    type-2 without argument with return type
def add1():
    a = int(input("Enter Number 1: "))
    b = int(input("Enter Number 2: "))
    return a+b
print(add1())

#type-3 with arguement without return type

def add2(x,y):
    print(x+y)

a = int(input("Enter Number 1: "))
b = int(input("Enter Number 2: "))
#add2(a,b)
#type-4 with arguement with return type

def add3(x,y):
    return x+y

a = int(input("Enter Number 1: "))
b = int(input("Enter Number 2: "))
print(add3(a,b))
