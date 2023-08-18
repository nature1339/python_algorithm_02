Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> "hi"
'hi'
>>> a = input()
hello
>>> a
'hello'
>>> type(a)
<class 'str'>
>>> l = []
>>> for _ in range(3):
	l.append(input())

	
hi
hellllllo
goooood
>>> l
['hi', 'hellllllo', 'goooood']
>>> l[0]
'hi'
>>> l[n]
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    l[n]
NameError: name 'n' is not defined
>>> n = 3
>>> l[n]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    l[n]
IndexError: list index out of range
>>> l = []
>>> n = 3
>>> for _ in range(n):
    l.append(input())
    print(l[0],l[n])

    
hi
Traceback (most recent call last):
  File "<pyshell#16>", line 3, in <module>
    print(l[0],l[n])
IndexError: list index out of range
>>> a = 'a
SyntaxError: EOL while scanning string literal
>>> a = 'a'=
SyntaxError: cannot assign to literal
>>> b= 'b'
>>> ab
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    ab
NameError: name 'ab' is not defined
>>> a='a'
>>> a
'a'
>>> b
'b'
>>> a+b
'ab'
>>> ord('a')
97
>>> ord('1')
49
>>> ord('0')
48
>>> chr(48)
'0'
>>> len()