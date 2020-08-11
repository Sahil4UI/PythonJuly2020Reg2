Python 3.7.8 (v3.7.8:4b47a5b6ba, Jun 27 2020, 04:47:50) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #list ->python Data Collection
>>> x = [1,2,3,4,5,"Avi","Nandani"]
>>> type(x)
<class 'list'>
>>> #Indexing
>>> x
[1, 2, 3, 4, 5, 'Avi', 'Nandani']
>>> x[0]
1
>>> x[1]
2
>>> x[3]
4
>>> x[-1]
'Nandani'
>>> a = [1,2,3,[4,5,6,7,[8,9,10],11],12]
>>> a[3]
[4, 5, 6, 7, [8, 9, 10], 11]
>>> a[3][4]
[8, 9, 10]
>>> a[3][4][2]
10
>>> x = [1,2,3,"hey","hi",["hello",4,5,[6,[7,[8, 9],10]]]]
>>> x[5][3][1][1][1]
9
>>> #Lit Slicing
>>> #list Slicing
>>> x = "python programming"
>>> x[0:6]
'python'
>>> x = [1,2,3,4,5,6,7,8,9,10]
>>> x[0:5]
[1, 2, 3, 4, 5]
>>> x[-1:-5]
[]
>>> x[-5:-1]
[6, 7, 8, 9]
>>>  x[-5:0]
 
SyntaxError: unexpected indent
>>> x[-5:0]
[]
>>> x[-5:]
[6, 7, 8, 9, 10]
>>> x[::-1]
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
>>> #LIST method
>>> x = []
>>> x.append(1)
>>> x
[1]
>>> x.append(2)
>>> x
[1, 2]
>>> x.append("Avi")
>>> x
[1, 2, 'Avi']
>>> x.append(12.34)
>>> x
[1, 2, 'Avi', 12.34]
>>> x.append(90)
>>> x
[1, 2, 'Avi', 12.34, 90]
>>> x.insert(1,200)
>>> x
[1, 200, 2, 'Avi', 12.34, 90]
>>> x.insert(4,"Nandani")
>>> x
[1, 200, 2, 'Avi', 'Nandani', 12.34, 90]
>>> x.pop()
90
>>> x
[1, 200, 2, 'Avi', 'Nandani', 12.34]
>>> x.pop()
12.34
>>> x
[1, 200, 2, 'Avi', 'Nandani']
>>> x.pop(3)
'Avi'
>>> x
[1, 200, 2, 'Nandani']
>>> x.remove(200)
>>> x
[1, 2, 'Nandani']
>>> x.remove(2)
>>> x
[1, 'Nandani']
>>> x
[1, 'Nandani']
>>> del x
>>> x
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    x
NameError: name 'x' is not defined
>>> x= [1,2,3,4,5,6,7,8,9,10]
>>> x.clear()
>>> x
[]
>>> x = [5,45,32,2,1,90,10,1000,90000,10000000]
>>> x.sort()
>>> x
[1, 2, 5, 10, 32, 45, 90, 1000, 90000, 10000000]
>>> x = [5,45,32,2,1,90,10,1000,90000,10000000]
>>> sorted(x)
[1, 2, 5, 10, 32, 45, 90, 1000, 90000, 10000000]
>>> x
[5, 45, 32, 2, 1, 90, 10, 1000, 90000, 10000000]
>>> x.sort()
>>> x
[1, 2, 5, 10, 32, 45, 90, 1000, 90000, 10000000]
>>> x.sort(reverse=True)
>>> x
[10000000, 90000, 1000, 90, 45, 32, 10, 5, 2, 1]
>>> x1 = ['a','b']
>>> x2 = ['c','d']
>>> x1.extend(x2)
>>> x1
['a', 'b', 'c', 'd']
>>> x2
['c', 'd']
>>> x2.extend(x1)
>>> x2
['c', 'd', 'a', 'b', 'c', 'd']
>>> x1
['a', 'b', 'c', 'd']
>>> x1
['a', 'b', 'c', 'd']
>>> x1.count('b')
1
>>> x2
['c', 'd', 'a', 'b', 'c', 'd']
>>> len(x2)
6
>>> x2 = ["how","are","you"]
>>> len(x2)
3
>>> len(x2[0])
3
>>> 