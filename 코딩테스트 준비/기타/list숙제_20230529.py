Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #• numbers라는 빈 리스트를 만들고 리스트를 출력한다.Type "help", "copyright", "credits" or "license()" for more information.
>>> numbers=[]
>>> numbers
[]
>>> numbers.append(1, 7, 3, 6, 5, 2, 13, 14)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    numbers.append(1, 7, 3, 6, 5, 2, 13, 14)
TypeError: list.append() takes exactly one argument (8 given)
>>> numbers
[]
>>> numbers.append(1)
>>> numbers.append(7)
>>> numbers.append(3)
>>> numbers.append(6)
>>> numbers.append(5)
>>> numbers.append(2)
>>> numbers.append(13)
>>> numbers.append(14)
>>> numbers
[1, 7, 3, 6, 5, 2, 13, 14]
>>> del odd (numbers):
	
SyntaxError: cannot delete function call
>>> 
KeyboardInterrupt
>>> del odd (numbers):
	
SyntaxError: cannot delete function call
>>> def odd_nbrs (numbers):
	 for i in numbers:
		 if i ! == 0:
			 
SyntaxError: invalid syntax
>>> def odd_nbrs (numbers):
	 for i in numbers:
		 if i % 2 !==0:
			 
SyntaxError: invalid syntax
>>> def odd_nbrs (numbers):
	 for i in numbers:
		 if i % 2 !=0
		 
SyntaxError: invalid syntax
>>> def odd_nbrs (numbers):
	 for i in numbers:
		 if i % 2 !=0:
			 numbers.remove(i)
	 return numbers

	
>>> 
>>> def odd_nbrs(numbers):
	for i in numbers:
		 if i % 2 !=0:
			 numbers.remove(i)
	 return numbers

SyntaxError: unindent does not match any outer indentation level
>>> def odd_nbrs(numbers):
	for i in numbers:
		if i % 2 !=0:
			numbers.remove(i)
	return numbers

>>> #답안나옴
>>> #numbers 리스트의 원소들 중 홀수는 모두 제 거한다. 그 후 다시 리스트를 출력한다.
>>> numbers[0, 20]
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    numbers[0, 20]
TypeError: list indices must be integers or slices, not tuple
>>> numbers(0, 20)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    numbers(0, 20)
TypeError: 'list' object is not callable
>>> numbers.insert(0, 20)
>>> 
>>> numbers
[20, 1, 7, 3, 6, 5, 2, 13, 14]
>>> numbers = []
>>> numbers = [1, 7, 3, 6, 5, 2, 13,14]
>>> i = 0
>>> while i < len(numbers):
	if numbers[i] % == 1:
		
SyntaxError: invalid syntax
>>> while i < len(numbers):
	if numbers[i] % 2 == 1:
		del numbers[i]
	else:
		i += 1

		
>>> print(numbers)
[6, 2, 14]
>>> def odd_nbrs(numbers):
	for i in numbers:
		if i % 2 !=0:
			numbers.remove(i)
	return numbers

>>> numbers = [1, 7, 3, 6, 5, 2, 13,14]
>>> odd_nbrs(numbers)
[7, 6, 2, 14]
>>> def odd_nbrs(numbers):
	for i in numbers:
		print('i: {i}')
		if i % 2 !=0:
			numbers.remove(i)
	return numbers

>>> numbers = [1, 7, 3, 6, 5, 2, 13,14]
>>> odd_nbrs(numbers)
i: {i}
i: {i}
i: {i}
i: {i}
[7, 6, 2, 14]
>>> def odd_nbrs(numbers):
	for i in numbers:
		print(f'i: {i}')
		if i % 2 !=0:
			numbers.remove(i)
	return numbers

>>> numbers = [1, 7, 3, 6, 5, 2, 13,14]
>>> odd_nbrs(numbers)
i: 1
i: 3
i: 5
i: 13
[7, 6, 2, 14]
>>> 