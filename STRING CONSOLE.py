Python 3.8.3 (v3.8.3:6f8c8320e9, May 13 2020, 16:29:34) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> String1 = "hello world"
>>> String1.lower()
'hello world'
>>> String1.upper()
'HELLO WORLD'
>>> String1.capitalize()
'Hello world'
>>> String1.title()
'Hello World'
>>> String.swapcase()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    String.swapcase()
NameError: name 'String' is not defined
>>> String1.swapcase()
'HELLO WORLD'
>>> String1 = "Hi How Are YOU?"
>>> String1.swapcase()
'hI hOW aRE you?'
>>> String1.center(20)
'  Hi How Are YOU?   '
>>> len(String1)
15
>>> String1.center(20,'*')
'**Hi How Are YOU?***'
>>> String1.center(20,'a')
'aaHi How Are YOU?aaa'
>>> String1.endswith('?')
True
>>> String1.startswith('H')
True
>>> String1.startswith('h')
False
>>> String1
'Hi How Are YOU?'
>>> String1.count('H')
2
>>> #python is a case sensitive
>>> String1.count('h')
0
>>> String2 ="aabbcchhhhhhhHHHH"
>>> String2.count("a")
2
>>> String2.count("b")
2
>>> String2.count("d")
0
>>> String2.count("h")
7
>>> String2.count("H")
4
>>> #Count method gives us the frequency of a character
>>> String3 = "C++ Programming Course"
>>> String3.replace("C++","Python")
'Python Programming Course'
>>> String3 =  String3.center(40)
>>> String3 =  String3.replace("C++","Python")
>>> String3
'         Python Programming Course         '
>>> String3.lstrip()
'Python Programming Course         '
>>> String3
'         Python Programming Course         '
>>> String3.rstrip()
'         Python Programming Course'
>>> String3.strip()
'Python Programming Course'
>>> String3 = "Python Programming Course"
>>> String3.center(40,"*")
'*******Python Programming Course********'
>>> String3.lstrip()
'Python Programming Course'
>>> Strip3.lstrip("*")
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    Strip3.lstrip("*")
NameError: name 'Strip3' is not defined
>>> String3.lstrip("*")
'Python Programming Course'
>>> String3
'Python Programming Course'
>>> String3=String3.center(40,'*')
>>> String3
'*******Python Programming Course********'
>>> String3.lstrip()
'*******Python Programming Course********'
>>> String3.lstrip("*")
'Python Programming Course********'
>>> String3.rstrip("*")
'*******Python Programming Course'
>>> String3.strip("*")
'Python Programming Course'
>>> String3
'*******Python Programming Course********'
>>> String3[0]
'*'
>>> String.index('P')
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    String.index('P')
NameError: name 'String' is not defined
>>> String3.index('P')
7
>>> String3.index(8,'P')
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    String3.index(8,'P')
TypeError: slice indices must be integers or None or have an __index__ method
>>> String3.index('P',8)
14
>>> String3
'*******Python Programming Course********'
>>> String3.find("P")
7
>>> String3.rfind("P")
14
>>> String3.rfind("z")
-1
>>> String3[14]
'P'
>>> String3[17]
'g'
>>> String4 = "hello hey hi"
>>> String4.find('h')
0
>>> String4.rfind('h')
10
>>> String4.find('h',1)
6
>>> String.find('z')
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    String.find('z')
NameError: name 'String' is not defined
>>> String4.find('z')
-1
>>> #-1 shows that character is not present in the string
>>> String4.index('z')
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    String4.index('z')
ValueError: substring not found
>>> String4
'hello hey hi'
>>> String3
'*******Python Programming Course********'
>>> String5 = "hellow Everyone, How are you ?"
>>> String5.split()
['hellow', 'Everyone,', 'How', 'are', 'you', '?']
>>> String5 =("hello")
>>> type(String5)
<class 'str'>
>>> String5 = ("hello","hi")
>>> type(String5)
<class 'tuple'>
>>> String = ("HELLO")
>>> String.split()
['HELLO']
>>> [HELLO]
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    [HELLO]
NameError: name 'HELLO' is not defined
>>> String5
('hello', 'hi')
>>> String5="hello how are u"
>>> String5 = String5.split()
>>> String5
['hello', 'how', 'are', 'u']
>>> String5[0]
'hello'
>>> String5[1]
'how'
>>> String[2]
'L'
>>> String5[2]
'are'
>>> String5[3]
'u'
>>> String6 = "*hello**how**are**you*"
>>> String6.split("*")
['', 'hello', '', 'how', '', 'are', '', 'you', '']
>>> String6 = "hello**how**are**you*"
>>> String6.split("**")
['hello', 'how', 'are', 'you*']
>>> text = "ram is a good boy"
>>> len(text)
17
>>> text.zfill(20)
'000ram is a good boy'
>>> text.zfill(45)
'0000000000000000000000000000ram is a good boy'
>>> text.zfill(45,1)
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    text.zfill(45,1)
TypeError: zfill() takes exactly one argument (2 given)
>>> 