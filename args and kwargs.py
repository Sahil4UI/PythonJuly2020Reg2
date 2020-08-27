'''
def studentRecord(Id,Name,*args):
    print(Id,Name,args)

studentRecord(101,"Nandani","9876543210","New Delhi","110043")
'''
'''
#** ->keyworded argument
def studentRecord(Id,Name,**kwargs):
    print(Id,Name,kwargs)

studentRecord(101,"Nandani",contactNo ="9876543210",Address="New Delhi",Pin="110043")
'''

def mainFunction():
    def f1():
        print("i am inside f1")
    def f2():
        print("i am inside f2")
    def f3():
        print("i am inside f3")
    def f4():
        print("i am inside f4")
    return f1,f2,f3,f4
'''
a,b,c,d = mainFunction()
a()
b()
c()
d()
'''
k = mainFunction()
print(k[3])
    
