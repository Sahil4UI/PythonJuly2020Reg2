#write
#acess mode = r(read),w(write),a(append)
#file = open("mytext.txt","w")

#data = "Python is a Programming  Language"

#data = "HOw are you ?"
data = "\nnandini is a good girl"
'''
file.write(data)

file.close()
'''
'''
with open('mytext1.txt',"a") as file:
    file.write(data)
'''

with open('mytext1.txt','r') as file:
    #data = file.read(10)
    #data = file.readline(2)
    data = file.readlines()

    for line in data:
        print(line)
