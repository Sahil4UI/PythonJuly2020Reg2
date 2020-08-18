Python 3.8.5 (v3.8.5:580fbb018f, Jul 20 2020, 12:11:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #List-mutable
>>> tup1 = (1,2,3)
>>> tup1[0]=1000
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    tup1[0]=1000
TypeError: 'tuple' object does not support item assignment
>>> #tuple-immutable
>>> tup2 = 1,2,3,4,5
>>> type(tup2)
<class 'tuple'>
>>> tup1 = 1
>>> type(tup1)
<class 'int'>
>>> tup2
(1, 2, 3, 4, 5)
>>> del tup2
>>> tup2
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    tup2
NameError: name 'tup2' is not defined
>>> tup3 = 1,2,3,"hi"
>>> tup3
(1, 2, 3, 'hi')
>>> tup3[0]
1
>>> tup3[-1]
'hi'
>>> tup3[-2]
3
>>> tup4 = (1,2,3,(4,5,6,(7,8)))
>>> tup4
(1, 2, 3, (4, 5, 6, (7, 8)))
>>> tup4[3][3][1]
8
>>> tup1 = (1,2,3,4,5,6,7,8,9,10)
>>> tup1[::2]
(1, 3, 5, 7, 9)
>>> tup1[1:6]
(2, 3, 4, 5, 6)
>>> tup1[::-1]
(10, 9, 8, 7, 6, 5, 4, 3, 2, 1)
>>> tup = (1,1,1,2,2,3,3,3,3,3)
>>> len(tup)
10
>>> tup.count(2)
2
>>> tup.count(3)
5
>>> tup
(1, 1, 1, 2, 2, 3, 3, 3, 3, 3)
>>> tup.index(1)
0
>>> tup = (1,2,2,3,4,5,2)
>>> tup.index(2)
1
>>> tup.index(3)
3
>>> tup.index(2,3)
6
>>> tup.index(10000)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    tup.index(10000)
ValueError: tuple.index(x): x not in tuple
>>> list1 = [1,90,100,0,-1]
>>> sorted(list1)
[-1, 0, 1, 90, 100]
>>> list1
[1, 90, 100, 0, -1]
>>> list1.sort()
>>> list1
[-1, 0, 1, 90, 100]
>>> t2 = 101,-1000,-1,-10,-8,100,200,1000,80,500
>>> sorted(t2)
[-1000, -10, -8, -1, 80, 100, 101, 200, 500, 1000]
>>> sorted(t2,reverse=True)
[1000, 500, 200, 101, 100, 80, -1, -8, -10, -1000]
>>> #Dictionary
>>> x= {"a":"apple"}
>>> x
{'a': 'apple'}
>>> type(x)
<class 'dict'>
>>> x = {101:"Ram",102:"Shyam",103:"Ravi",104:"amit"}
>>> x
{101: 'Ram', 102: 'Shyam', 103: 'Ravi', 104: 'amit'}
>>> x[101] = "Rahul"
>>> x
{101: 'Rahul', 102: 'Shyam', 103: 'Ravi', 104: 'amit'}
>>> x[0]
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    x[0]
KeyError: 0
>>> x[101]
'Rahul'
>>> x[104]
'amit'
>>> x[105] = "Rohit"
>>> x
{101: 'Rahul', 102: 'Shyam', 103: 'Ravi', 104: 'amit', 105: 'Rohit'}
>>> x
{101: 'Rahul', 102: 'Shyam', 103: 'Ravi', 104: 'amit', 105: 'Rohit'}
>>> 
>>> del x[105]
>>> x
{101: 'Rahul', 102: 'Shyam', 103: 'Ravi', 104: 'amit'}
>>> x
{101: 'Rahul', 102: 'Shyam', 103: 'Ravi', 104: 'amit'}
>>> x.keys()
dict_keys([101, 102, 103, 104])
>>> x.values()
dict_values(['Rahul', 'Shyam', 'Ravi', 'amit'])
>>> x.items()
dict_items([(101, 'Rahul'), (102, 'Shyam'), (103, 'Ravi'), (104, 'amit')])
>>> x.pop(101)
'Rahul'
>>> x
{102: 'Shyam', 103: 'Ravi', 104: 'amit'}
>>> x.popitem()
(104, 'amit')
>>> x
{102: 'Shyam', 103: 'Ravi'}
>>> x.popitem()
(103, 'Ravi')
>>> x.clear()
>>> x
{}
>>> del x
>>> x
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    x
NameError: name 'x' is not defined
>>> x= {"a":1,"b":2}
>>> y = x.copy()
>>> id(x)
140708132743232
>>> id(y)
140708132735424
>>> y=x
>>> id(x)
140708132743232
>>> id(y)
140708132743232
>>> x
{'a': 1, 'b': 2}
>>> x.update({'c':3})
>>> x
{'a': 1, 'b': 2, 'c': 3}
>>> x.get('a')
1
>>> x.get('c')
3
>>> x = ["a","b","c","d"]
>>> y = 0
>>> z =dict.fromkeys(x,y)
>>> z
{'a': 0, 'b': 0, 'c': 0, 'd': 0}
>>> z =dict.fromkeys(x,1)
>>> z
{'a': 1, 'b': 1, 'c': 1, 'd': 1}
>>> 