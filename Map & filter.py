def CelToFah(tempInCelcius):
    return 9/5*tempInCelcius+32

temperatures = [30.56,40,28.9,18.40,0,51,43,58.9]
'''
f_temp = []
for temp in temperatures:
    f= CelToFah(temp)
    f_temp.append(f)

print(f_temp)
'''
'''
x = list(map(CelToFah,temperatures))
print(x)
'''
#lambda function
'''
a = lambda x: 9/5*x+32
print(a(30))

n= lambda a,b,c: a if a>b else b if b>c else c
print(n(100,1000,-100))
'''
tkinter
p= [lambda i=i:i for i in range(1,100)]
for x in p:
    print(x())
    
#filter function


