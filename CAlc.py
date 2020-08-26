def add(a,b):
    print(a+b)

def sub(a,b):
    print(a-b)

def mul(a,b):
    print(a*b)

def div(a,b):
    print(a/b)

x = int(input("Enter Number 1 : "))
y = int(input("Enter Number 2 : "))

print(
"""
press 1 for addition
press 2 for subtraction
press 3 for multiplication
press 4 for division
""")
choice = int(input("Which Operation You wanna Perform ?"))
if choice==1:
    add(x,y)

print(k)
