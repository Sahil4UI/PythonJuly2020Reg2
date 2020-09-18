#access mode -> "rb","wb"
image = open("tom.jpeg","rb")
data = image.read()
print(data)
image.close()

file=open("tom1.txt","wb")
file.write(data)
file.close()

