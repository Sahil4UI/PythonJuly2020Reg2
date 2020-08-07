
x =1
while(x<=20):
    print(x)
    x+=2


#-h.w.
#-check wether number is prime or not
#-print 10 numbers of fibonacci series
#-reverse a number
#-sum of digits of number

#PrimeNumber
'''
number = int(input("Enter the number :"))

i=2
while(i<number):
    if number % i==0:
        print("Number is not prime")
        break
    i+=1
else:
    print("Number is Prime")
'''
#fibonacci SEries
'''
first=0
second=1
print(first,second,end=' ')

i=1
while(i<=8):
    third = first+second
    print(third,end=' ')
    first,second=second,third
    i+=1
'''
#Reverse of a number
number =int(input("Enter a number:"))
temp=number
length = len(str(number))
i=1
rev=0
while(i<=length):
    rem = number%10
    rev=rev*10+rem
    number = number//10
    i+=1
print(rev)
    
