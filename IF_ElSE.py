'''
number = int(input("enter number : "))
if number%2 != 0:
    print("odd number")
else:
    print("even number")
'''
'''
#we have a,b,c , find who is greatest
a = int(input("Enter number1 : "))
b = int(input("Enter number2 : "))
c = int(input("Enter number2 : "))

if a == b ==c:
    print("All are equal")
elif a > b and a > c:
    print(f"{a} is largest")
elif b >c:
    print(f"{b} is largest")
else:
    print(f"{c} is largest")
'''
#we have 3 sides of traingle ->a,b,c
#check wether traingle is equilateral,isoceles or scalene
a = int(input("Enter side 1: "))
b = int(input("Enter side 2: "))
c = int(input("Enter side 3: "))
if a+b>c and b+c>a and a+c>b:
    if a==b==c:
        print("equilateral traingle")
    elif a ==b or b==c or c==a:
        print("isoceles traingle")
    else:
        print("scalene traingle")
else:
    print("invalid traingle")
    











    
