Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> squares = [1,4,9,16,25]
>>> print(squares[0])
1
>>> print(squares[-1])
25
>>> print(squares[-2])
16
>>> print(squares[2::])
[9, 16, 25]
>>> print(squares[2:])
[9, 16, 25]
>>> print(squares[-3:])
[9, 16, 25]
>>> print(squares[0:])
[1, 4, 9, 16, 25]
>>> print(squares[:])
[1, 4, 9, 16, 25]
>>> print(squares)
[1, 4, 9, 16, 25]
>>> squares[1]=3
>>> print squares
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(squares)?
>>> squares
[1, 3, 9, 16, 25]
>>> squares.append(100)
>>> squares
[1, 3, 9, 16, 25, 100]
>>> squares[1]=4
>>> squares
[1, 4, 9, 16, 25, 100]
>>> squares.insert(1)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    squares.insert(1)
TypeError: insert expected 2 arguments, got 1
>>> squares.insert(1, 3)
>>> squares
[1, 3, 4, 9, 16, 25, 100]
>>> squares.remove(-1)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    squares.remove(-1)
ValueError: list.remove(x): x not in list
>>> squares.remove(4)
>>> squares
[1, 3, 9, 16, 25, 100]
>>> a = squares.remove(3)
>>> a
>>> a = squares.pop()
>>> a
100
>>> squares
[1, 9, 16, 25]
>>> b = squares.pop(1)
>>> b
9
>>> squares
[1, 16, 25]
>>> l = [1,3,2,6,34,7,5,20]
>>> I.sort
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    I.sort
NameError: name 'I' is not defined
>>> I.sort()
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    I.sort()
NameError: name 'I' is not defined
>>> l
[1, 3, 2, 6, 34, 7, 5, 20]
>>> l.sort()
>>> l
[1, 2, 3, 5, 6, 7, 20, 34]
>>> l.sort(-1)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    l.sort(-1)
TypeError: sort() takes no positional arguments
>>> l.reverse()
>>> l
[34, 20, 7, 6, 5, 3, 2, 1]
>>> l.clear()
>>> l
[]
>>> l = []
>>> l1 = [1,2,3]
>>> l2 = [4,5,6]
>>> l3 = l1 + l2
>>> l3
[1, 2, 3, 4, 5, 6]
>>> l4 = []
>>> l4.append(l1)
>>> l4
[[1, 2, 3]]
>>> l4.append(l2)
>>> l4
[[1, 2, 3], [4, 5, 6]]
>>> l1 + l2
[1, 2, 3, 4, 5, 6]
>>> l1
[1, 2, 3]
>>> l2
[4, 5, 6]
>>> l1.extend(l2)
>>> l1
[1, 2, 3, 4, 5, 6]
>>> l2
[4, 5, 6]
>>> len(l1)= 2
SyntaxError: cannot assign to function call
>>> len(l1)
6
>>> range(l1)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    range(l1)
TypeError: 'list' object cannot be interpreted as an integer
>>> range(len(l1))
range(0, 6)
>>> for i in range(len(l1)):
	print(l[i])

	
Traceback (most recent call last):
  File "<pyshell#64>", line 2, in <module>
    print(l[i])
IndexError: list index out of range
>>> for i in range(len(l1)):
	print(l1[i])

	
1
2
3
4
5
6
>>> for i in range(len(l1)):
	print(f'index: {i}, value: {l1[i]}')

	
index: 0, value: 1
index: 1, value: 2
index: 2, value: 3
index: 3, value: 4
index: 4, value: 5
index: 5, value: 6
>>> 