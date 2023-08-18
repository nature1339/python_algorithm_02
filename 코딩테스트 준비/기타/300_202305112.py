Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> ; = []
SyntaxError: invalid syntax
>>> l = []
>>> import random
>>> for i in range(100):
	l.append(random.randint(1, 50))

	
>>> l.remove()
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    l.remove()
TypeError: list.remove() takes exactly one argument (0 given)
>>> t = []
>>> for i in l:
	if i not in t:
		t.append(i)

		
>>> print(t)
[47, 31, 7, 16, 20, 37, 17, 28, 11, 43, 33, 39, 29, 5, 1, 2, 9, 18, 23, 3, 13, 26, 15, 19, 25, 42, 4, 40, 34, 30, 27, 50, 44, 32, 48, 12, 35, 46, 14, 6, 22]
>>> t
[47, 31, 7, 16, 20, 37, 17, 28, 11, 43, 33, 39, 29, 5, 1, 2, 9, 18, 23, 3, 13, 26, 15, 19, 25, 42, 4, 40, 34, 30, 27, 50, 44, 32, 48, 12, 35, 46, 14, 6, 22]
>>> for i in range(len(t) - 1):
	for j in range(len(t)):
		if t[j] > t[j + 1]
		
SyntaxError: invalid syntax
>>> for i in range(len(t) - 1):
	for j in range(len(t)):
		if t[j] > t[j + 1]:
			tmp = t[j + 1]
			t[j + 1] = t[j]
			t[j] = tmp

			
Traceback (most recent call last):
  File "<pyshell#27>", line 3, in <module>
    if t[j] > t[j + 1]:
IndexError: list index out of range
>>> for i in range(len(t) - 1, 0, -1):
	for j in range(len(i)):
		if t[j] > t[j + 1]:
			tmp = t[j + 1]
			t[j + 1] = t[j]
			t[j] = tmp

			
Traceback (most recent call last):
  File "<pyshell#29>", line 2, in <module>
    for j in range(len(i)):
TypeError: object of type 'int' has no len()
>>> 
>>> t
[31, 7, 16, 20, 37, 17, 28, 11, 43, 33, 39, 29, 5, 1, 2, 9, 18, 23, 3, 13, 26, 15, 19, 25, 42, 4, 40, 34, 30, 27, 47, 44, 32, 48, 12, 35, 46, 14, 6, 22, 50]
>>> for i in range(len(t) - 1, 0, -1):
	for j in range(len(i)):
		if t[j] > t[j + 1]:
			t[j], t[j + 1] = t[j + 1], t[j]

			
Traceback (most recent call last):
  File "<pyshell#34>", line 2, in <module>
    for j in range(len(i)):
TypeError: object of type 'int' has no len()
>>> for i in range(len(t) - 1, 0, -1):
	for j in range(i):
		if t[j] > t[j + 1]:
			t[j], t[j + 1] = t[j + 1], t[j]

			
>>> t
[1, 2, 3, 4, 5, 6, 7, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 22, 23, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 39, 40, 42, 43, 44, 46, 47, 48, 50]
>>> len(t) - 1 # 맨끝 인덱스
40
>>> 0 # 직전까지 즉 1까지
0
>>> for j in range(len(i)): #i 직전까지 가라
	#버블 정렬

3 80 list 합
SyntaxError: expected an indented block
>>> l = []
>>> for i in range(3, 81):
	l.append(i)

	
>>> sum = 0
>>> for i in l:
        sum += i
    print(sum)
    
SyntaxError: unindent does not match any outer indentation level
>>> sum = 0
>>> for i in l:
	sum += i

	
>>> print(sum)
3237
>>> 
>>> l = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
>>> t
[1, 2, 3, 4, 5, 6, 7, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 22, 23, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 39, 40, 42, 43, 44, 46, 47, 48, 50]
>>> set(t)
{1, 2, 3, 4, 5, 6, 7, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 22, 23, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 39, 40, 42, 43, 44, 46, 47, 48, 50}
>>> t2
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    t2
NameError: name 't2' is not defined
>>> t
[1, 2, 3, 4, 5, 6, 7, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 22, 23, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 39, 40, 42, 43, 44, 46, 47, 48, 50]
>>> l2 = []
>>> for i in range(100):
	l2.append(random.randint(1, 50))

	
>>> l2
[37, 49, 19, 19, 45, 22, 32, 15, 33, 26, 37, 45, 41, 5, 9, 8, 29, 12, 21, 24, 8, 40, 39, 39, 43, 14, 44, 26, 41, 4, 49, 42, 15, 29, 32, 41, 39, 6, 13, 41, 28, 45, 20, 6, 27, 49, 23, 36, 29, 47, 23, 12, 14, 16, 22, 14, 20, 50, 44, 38, 28, 31, 23, 19, 43, 19, 3, 12, 49, 9, 26, 10, 33, 13, 14, 21, 12, 19, 27, 17, 36, 41, 41, 50, 15, 15, 15, 24, 35, 38, 29, 11, 23, 36, 35, 35, 14, 7, 30, 40]
>>> l3 =  set(l2)
>>> l3
{3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 19, 20, 21, 22, 23, 24, 26, 27, 28, 29, 30, 31, 32, 33, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 47, 49, 50}
>>> d = {'name': 'Steve', 'age': 10}
>>> l = []
>>> l = [-1]
>>> for i in range(6):
	num = -1
	while num in l:
		num = random.randint(1,45)
	l.append(num)

	
>>> l
[-1, 34, 42, 29, 43, 6, 25]
>>> l.remove(-1)
>>> l
[34, 42, 29, 43, 6, 25]
>>> l.sort()
>>> l
[6, 25, 29, 34, 42, 43]
>>> 