Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> [1,2,3,a,b,c]
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    [1,2,3,a,b,c]
NameError: name 'a' is not defined
>>> l = [1,2,3,'a','b','c']
>>> l[1]
2
>>> l[1] = 20
>>> l
[1, 20, 3, 'a', 'b', 'c']
>>> append(30)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    append(30)
NameError: name 'append' is not defined
>>> l.append(30)
>>> l
[1, 20, 3, 'a', 'b', 'c', 30]
>>> add[2]=30
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    add[2]=30
NameError: name 'add' is not defined
>>> l.insert(2,50)
>>> l
[1, 20, 50, 3, 'a', 'b', 'c', 30]
>>> l.delete(a)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    l.delete(a)
AttributeError: 'list' object has no attribute 'delete'
>>> l.delete('a')
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    l.delete('a')
AttributeError: 'list' object has no attribute 'delete'
>>> l.remove(a)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    l.remove(a)
NameError: name 'a' is not defined
>>> l.remove('a')
>>> l
[1, 20, 50, 3, 'b', 'c', 30]
>>> l.delete[2]
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    l.delete[2]
AttributeError: 'list' object has no attribute 'delete'
>>> l.delete(2)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    l.delete(2)
AttributeError: 'list' object has no attribute 'delete'
>>> del l[3]
>>> l
[1, 20, 50, 'b', 'c', 30]
>>> a = 30
>>> a
30
>>> del a
>>> a
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> a = l.pop
>>> a = l.pop()
>>> a
30
>>> l
[1, 20, 50, 'b', 'c']
>>> a = l.pop(2)
>>> a
50
>>> 'a' in l
False
>>> 'a' not in l
True
>>> import random
>>> random.randint(1, 100)
72
>>> l = []
>>> l
[]
>>> for i in range(100):
	l.append(random.randint(1,100))

	
>>> l
[71, 83, 22, 98, 68, 74, 3, 83, 38, 13, 33, 18, 16, 40, 2, 99, 38, 69, 28, 27, 66, 80, 45, 51, 42, 29, 80, 19, 63, 78, 8, 30, 34, 46, 38, 73, 28, 66, 29, 32, 38, 1, 25, 45, 14, 94, 7, 5, 21, 52, 58, 23, 75, 26, 98, 5, 15, 13, 99, 8, 60, 30, 34, 50, 80, 40, 90, 42, 33, 67, 21, 40, 17, 12, 47, 34, 53, 45, 45, 12, 74, 92, 77, 3, 59, 34, 13, 6, 53, 93, 4, 8, 97, 83, 72, 41, 17, 45, 62, 8]
>>> n = []
>>> for i in l:
	print(i, end=' ')

	
71 83 22 98 68 74 3 83 38 13 33 18 16 40 2 99 38 69 28 27 66 80 45 51 42 29 80 19 63 78 8 30 34 46 38 73 28 66 29 32 38 1 25 45 14 94 7 5 21 52 58 23 75 26 98 5 15 13 99 8 60 30 34 50 80 40 90 42 33 67 21 40 17 12 47 34 53 45 45 12 74 92 77 3 59 34 13 6 53 93 4 8 97 83 72 41 17 45 62 8 
>>> for i in l:
	if i not in n:
		n.append(i)

		
>>> 
>>> n
[71, 83, 22, 98, 68, 74, 3, 38, 13, 33, 18, 16, 40, 2, 99, 69, 28, 27, 66, 80, 45, 51, 42, 29, 19, 63, 78, 8, 30, 34, 46, 73, 32, 1, 25, 14, 94, 7, 5, 21, 52, 58, 23, 75, 26, 15, 60, 50, 90, 67, 17, 12, 47, 53, 92, 77, 59, 6, 93, 4, 97, 72, 41, 62]
>>> 