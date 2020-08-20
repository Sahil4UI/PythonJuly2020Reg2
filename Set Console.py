Python 3.7.8 (v3.7.8:4b47a5b6ba, Jun 27 2020, 04:47:50) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #SET
>>> a = {'a','b'}
>>> type(a)
<class 'set'>
>>> a[0]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    a[0]
TypeError: 'set' object is not subscriptable
>>> #Set - >an unordered Data Collection of Python
>>> set1 = {'a','b','c','d'}
>>> set1
{'d', 'b', 'c', 'a'}
>>> set1
{'d', 'b', 'c', 'a'}
>>> for i in set1:
	print(i)

d
b
c
a
>>> set1
{'d', 'b', 'c', 'a'}
>>> set1.add('e')
>>> set1
{'c', 'd', 'b', 'a', 'e'}
>>> set1.add('f')
>>> set1
{'f', 'c', 'd', 'b', 'a', 'e'}
>>> set1.update(["g","h","i","j"])
>>> set1
{'f', 'c', 'j', 'h', 'd', 'g', 'b', 'i', 'a', 'e'}
>>> set1.update(["k"])
>>> set1
{'f', 'c', 'j', 'h', 'd', 'g', 'b', 'i', 'k', 'a', 'e'}
>>> set1.update("l","m")
>>> set1
{'f', 'l', 'c', 'j', 'h', 'd', 'g', 'b', 'i', 'k', 'a', 'e', 'm'}
>>> sort(set1)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    sort(set1)
NameError: name 'sort' is not defined
>>> sorted(set1)
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
>>> sorted(set1,reverse=True)
['m', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']
>>> reversed(sorted(set1,reverse=True))
<list_reverseiterator object at 0x7fab438e0e10>
>>> for i in range(1,11):
	print(i)

1
2
3
4
5
6
7
8
9
10
>>> for i in reversed(range(1,11)):
	print(i)

10
9
8
7
6
5
4
3
2
1
>>> set1
{'f', 'l', 'c', 'j', 'h', 'd', 'g', 'b', 'i', 'k', 'a', 'e', 'm'}
>>> len(set1)
13
>>> set1.discard("j")
>>> set1
{'f', 'l', 'c', 'h', 'd', 'g', 'b', 'i', 'k', 'a', 'e', 'm'}
>>> set1.discard("b")
>>> set1.discard("z")
>>> set1
{'f', 'l', 'c', 'h', 'd', 'g', 'i', 'k', 'a', 'e', 'm'}
>>> set1 = {1,1,1,1}
>>> set1
{1}
>>> #Set cannot contain redundant values(duplicate)
>>> set1
{1}
>>> set1 = {'a','b','c','d'}
>>> set1.pop()
'd'
>>> set1
{'b', 'c', 'a'}
>>> set1.clear()
>>> set1
set()
>>> del set1
>>> set1
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    set1
NameError: name 'set1' is not defined
>>> list1 = [1,2,3]
>>> list1.pop(0)
1
>>> set1={'a','b','c','d'}
>>> set2 = {'a','d','e','f','g'}
>>> set1.union(set2)
{'f', 'c', 'd', 'g', 'b', 'a', 'e'}
>>> set1.update(set2)
>>> set1
{'f', 'c', 'd', 'g', 'b', 'a', 'e'}
>>> set2
{'f', 'g', 'd', 'a', 'e'}
>>> set1.intersection(set2)
{'f', 'g', 'd', 'a', 'e'}
>>> set1 = {1,2,3,4}
>>> set2 = {2,3,5,9}
>>> set1.intersection(set2)
{2, 3}
>>> set1
{1, 2, 3, 4}
>>> set2
{9, 2, 3, 5}
>>> set1.difference(set2)
{1, 4}
>>> set2.difference(set1)
{9, 5}
>>> set1
{1, 2, 3, 4}
>>> set2
{9, 2, 3, 5}
>>> set1.difference_update(set2)
>>> set1
{1, 4}
>>> set1
{1, 4}
>>> set2
{9, 2, 3, 5}
>>> set1 = {1,2,3,4,5}
>>> set2 = {4,5,6,7,8}
>>> set1.intersection_update(set2)
>>> set1
{4, 5}
>>> set3 = set1.copy()
>>> id(set1)
140373548662128
>>> id(set3)
140373548660928
>>> set4 = set1
>>> id(set1)
140373548662128
>>> id(set4)
140373548662128
>>> x = {{'a','b'},{'c','d'}}
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    x = {{'a','b'},{'c','d'}}
TypeError: unhashable type: 'set'
>>> set1
{4, 5}
>>> set1 = {1,2,3,4,5,6,7,8,9,10}
>>> set2 = {1,2,3,4}
>>> set1.issubset(set2)
False
>>> set2.issubset(set1)
True
>>> #subset is the smaller part of the set
>>> list1 = [1,2,3]
>>> set(list1)
{1, 2, 3}
>>> 