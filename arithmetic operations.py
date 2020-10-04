Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 2+3
5
>>> 9-8
1
>>> 80*2
160
>>> 8/2
4.0
>>> 5//2
2
>>>  8+9-10
 
SyntaxError: unexpected indent
>>> 8 + 9 - 10
7
>>> 8+2*3
14
>>> (8+2)*3
30
>>> 2 * 2 *2
8
>>> 2 ** 3
8
>>> 2 *** 3
SyntaxError: invalid syntax
>>> 2 ** 4
16
>>> 10 // 3
3
>>> 10 / 3
3.3333333333333335
>>> 10  % 3
1
>>> ' bhoomi "
SyntaxError: EOL while scanning string literal
>>> 'bhoomi'
'bhoomi'
>>> print('bhoomi')
bhoomi
>>> print('bhooomi's laptop')
      
SyntaxError: invalid syntax
>>> print("bhoomi's laptop")
bhoomi's laptop
>>> print("bhoomi "laptop"")
SyntaxError: invalid syntax
>>> print('bhoomi "laptop"')
bhoomi "laptop"
>>> print("bhoomi's "laptop"")
SyntaxError: invalid syntax
>>> print('bhoomi\'s "laptop"')
bhoomi's "laptop"
>>> 'bhoomi'+'bhoomi'
'bhoomibhoomi'
>>> 10 * 'bhoomi'
'bhoomibhoomibhoomibhoomibhoomibhoomibhoomibhoomibhoomibhoomi'
>>> print('c:\docs\bhoomi')
c:\docshoomi
>>> print('c:\docs\nobita')
c:\docs
obita
>>> print(r'c:\docs\nobita')
c:\docs\nobita
>>> x=2
>>> x+3
5
>>> y=3
>>> x+y
5
>>> x=9
>>> x+y
12
>>> abc
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    abc
NameError: name 'abc' is not defined
>>> x+10
19
>>> 19+y
22
>>> -+y
-3
>>> _ + y
0
>>> x+y
12
>>> _ + 2
14
>>> //underscore represent output of the previous operation
SyntaxError: invalid syntax
>>> name='bhoomi'
>>> 
>>> name
'bhoomi'
>>> name + 'model'
'bhoomimodel'
>>> name + ' model '
'bhoomi model '
>>> name[0]
'b'
>>> name[6]
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    name[6]
IndexError: string index out of range
>>> name[5]
'i'
>>> name[-1]
'i'
>>> // if we use minus range in aaray index it will start form reverse order that is left to right.
SyntaxError: invalid syntax
>>> name[-2]
'm'
>>> name[0:2]
'bh'
>>> name[0:4]
'bhoo'
>>> name[1:3]
'ho'
>>> name[1:4]
'hoo'
>>> name[1:]
'hoomi'
>>> name[3:]
'omi'
>>> name[:4]
'bhoo'
>>> name[:2]
'bh'
>>> name[2:15]
'oomi'
>>> //using this we can avoide error
SyntaxError: invalid syntax
>>> name[0:3]='my'
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    name[0:3]='my'
TypeError: 'str' object does not support item assignment
>>> name[0]='m'
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    name[0]='m'
TypeError: 'str' object does not support item assignment
>>> // we can not change string's value
SyntaxError: invalid syntax
>>> //string in python is immutable
SyntaxError: invalid syntax
>>> 'my' + name[]
SyntaxError: invalid syntax
>>> my + name[2:]
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    my + name[2:]
NameError: name 'my' is not defined
>>> 'my' + name[2:]
'myoomi'
>>> myname='bhoomi'
>>> len(myname)
6
>>> 