#Linear Search
list1 = [1,0,-1000,40,50,60,-20,100,200,400,500,600]

choice  = int(input("Enter Choice : "))
'''
for i in range(0,len(list1)):
    if choice == list1[i]:
        print("Found")
        break
else:
    print("Not Found")
'''
'''
for value in list1:
    if choice == value:
        print("Found")
        break
else:
    print("Not Found")
'''

if choice in list1:
    print("Found")
else:
    print("Not Found")
