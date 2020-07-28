#we have three sides a,b,c and
#check wether traingle is equilateral , isoceles,Scalene
#nested if-else:

a = int(input("Enter SIDE 1:"))
b = int(input("Enter SIDE 2:"))
c = int(input("Enter SIDE 3:"))

if a+b>c and b+c>a and c+a>b:
    if a ==b and b==c:
        print("Equilateral traingle")
    elif a==b or b==c or c==a:
        print("isoceles Traingle")
    else:
        print("scalene Traingle")

else:
    print("Traingle is invalid")
        
    
    
    
