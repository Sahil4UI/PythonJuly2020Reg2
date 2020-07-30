#print fibonacci series
#            0 1 1 2 3 5 8 13.......
#check wether number is prime or not
#check wether number is armstrong number ->(153 -> )
#find the sum of digits of number ->123 ->1+2+3=>6


#fibonacci Series
#0 1 1 2 3 5
'''
first = 0
second = 1
print(first)
print(second)

for i in range(1,9):
    third = first+second
    print(third)
    first = second
    second = third
'''
'''
number = int(input("Enter number"))

for i in range(2,number):
    if number % i ==0:
        print("Number is not Prime")
        break
else:
    print("Prime")
'''
#sum of digits of number
'''
number = int(input("Enter number"))
sum1 = 0
for i in range(len(str(number))):
    rem = number%10
    sum1=sum1+rem
    number = number//10
print(sum1)
'''
#armstrong Number
number = int(input("Enter number"))
temp = number
sum1 = 0
for i in range(len(str(number))):
    rem = number%10
    sum1=sum1+rem**3
    number = number//10

if (temp == sum1):
    print("Armstrong number")
else:
    print("Not an Armstrong Number")

    




