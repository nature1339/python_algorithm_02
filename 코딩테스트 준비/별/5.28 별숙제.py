Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> for i in range(1, 6):
	for j in range(5):
	    print("*", end=" ")

	    
* * * * * * * * * * * * * * * * * * * * * * * * * 
>>> > for i in range(1, 6):
	for j in range(5):
		
SyntaxError: invalid syntax
>>> for i in range(1, 6):
	for j in range(5):
	    print("*")

	    
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
>>> 
>>> for i in range(1, 6):
	for j in range(5):
	    print("*"*j, end=" ")

	    
 * ** *** ****  * ** *** ****  * ** *** ****  * ** *** ****  * ** *** **** 
>>> for i in range(1, 6):
	for j in range(5):
	    print("*"*j, end=" ")
	print(end = " ")

	
 * ** *** ****   * ** *** ****   * ** *** ****   * ** *** ****   * ** *** ****  \
>>> for i in range(1, 6):
	for j in range(5):
	    print("*"*j, end="")	    

	
**************************************************
>>> 
>>> for i in range(1, 6):
	for j in range(5):
	    print("*"*j, end=" ")

	    
 * ** *** ****  * ** *** ****  * ** *** ****  * ** *** ****  * ** *** **** 
>>> for i in range(1, 6):
	for j in range(i):
	    print("*"*j, end=" ")

	    
  *  * **  * ** ***  * ** *** **** 
>>> for i in range(1, 6):
	for j in range(i):
	    print("*"*j, end=" ")
	print()

	
 
 * 
 * ** 
 * ** *** 
 * ** *** **** 
>>> for i in range(1, 6):
	for j in range(i):
	    print("*", end=" ")
    print()
    
SyntaxError: unindent does not match any outer indentation level
>>> for i in range(1, 6):
	for j in range(i):
	    print("*", end=" ")
        print()
        
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> 
>>> for i in range(1, 6):
	for j in range(i):
	    print("*", end=" ")
        print()
        
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> for i in range(1, 6):
	for j in range(i):
	    print("*", end=" ")

	    
* * * * * * * * * * * * * * * 
>>> for i in range(1, 6):
	for j in range(i):
	    print("*", end=" ")
	print()

	
* 
* * 
* * * 
* * * * 
* * * * * 
>>> for i in range(1, 6):
	for j in range(i):
	    print(end=" "+"*", end=" ")
	print()
	
SyntaxError: keyword argument repeated: end
>>> for i in range(1, 6):
	for j in range(i):
	    print(end="")
	    print("*", end=" ")
	print()

	
* 
* * 
* * * 
* * * * 
* * * * * 
>>> for i in range(1, 6):
	for j in range(i):
	    print(end=""*(5-i))
	    print("*", end=" ")
	print()

	
* 
* * 
* * * 
* * * * 
* * * * * 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> for i in range(1, 6):
	for j in range(5-i):
	    print(end="")
	for j in range(i):
	    print("*", end="")
	print()

	
*
**
***
****
*****
>>> for i in range(1, 6):
	for j in range(5-i):
	    print(' ', end="")
	for j in range(i):
	    print("*", end="")
	print()

    *
   **
  ***
 ****
*****
>>> for i in range(1, 6):
	for j in range(5-i):
	    print(" ", end="")
	for j in range(i):
	    print("*", end="")
	for j in range(5-i)
	
SyntaxError: invalid syntax
>>> for i in range(1, 6):
	for j in range(5-i):
	    print(" ", end="")
	for j in range(i):
	    print("*", end="")
	for j in range(5-i):
	    print(" ", end="")
	print()

	
    *    
   **   
  ***  
 **** 
*****
>>> for i in range(1, 6):
	for j in range(5-i):
	    print(" ", end="")
	for j in range(5-i):
	    print("*", end="")
	for j in range(5-i):
	    print(" ", end="")
	print()

	
    ****    
   ***   
  **  
 * 

>>> for i in range(1, 6):
	for j in range(5-i):
	    print(" ", end="")
	for j in range(i):
	    print("*", end="")
	for j in range(5-i):
	    print(" ", end="")
	print()

	
    *    
   **   
  ***  
 **** 
*****
>>> 
================================ RESTART: Shell ================================
>>> print()

>>>  for i in range(1, 6):
	for j in range(5-i):
		print(" ", end="")
	for j in range(i):
		if i // 2 != 0:
			print("*", end="")
	for j in range(5-i):
		print(" ", end="")
	print()
	
SyntaxError: unexpected indent
>>> for i in range(1, 6):
	for j in range(5-i):
		print(" ", end="")
	for j in range(i):
		if i // 2 != 0:
			print("*", end="")
	for j in range(5-i):
		print(" ", end="")
	print()

	
        
   **   
  ***  
 **** 
*****
>>> for i in range(1, 6):
	for j in range(5-i):
		print(" ", end="")
	for j in range(i):
		if i / 2 != 0:
			print("*", end="")
	for j in range(5-i):
		print(" ", end="")
	print()

	
    *    
   **   
  ***  
 **** 
*****
>>> for i in range(1, 6):
	for j in range(5-i):
		print(" ", end="")
	for j in range(i):
		if i % 2 != 0:
			print("*", end="")
	for j in range(5-i):
		print(" ", end="")
	print()

	
    *    
      
  ***  
  
*****
>>> for i in range(1, 6):
	for j in range(5-i):
		print(" ", end="")
	for j in range(i):
		print("*", end="")
	for j in range(5-i):
		print(" ", end="")
	print()

	
    *    
   **   
  ***  
 **** 
*****
>>> for i in range(1, 6):
	for j in range(5-i):
		print(" ", end="")
	for j in range(i):
		print("*", end="")
	for j in range(i-1):
		print("*", end="")
	print()

    *
   ***
  *****
 *******
*********

>>> for i in range(6, 1):
	for j in range(i):
		print(" ", end="")
	for j in range(i):
		print("*", end="")
	for j in range(i-1):
		print("*", end="")		
	print()

>>> for i in range(5, 0,-1):
	for j in range(i):
		print(" ", end="")
	for j in range(i):
		print("*", end="")
	for j in range(i-1):
		print("*", end="")		
	print()

	
     *********
    *******
   *****
  ***
 *
>>> 
KeyboardInterrupt
>>> for i in range(5, 0, -1):
	for j in range(5-i):
		print(" ", end="")
	for j in range(i):
		print("*", end="")
	for j in range(i-1):
		print("*", end="")
	print()

*********
 *******
  *****
   ***
    *
>>> for i in range(4, 0, -1):
	for j in range(5-i):
		print(" ", end="")
	for j in range(i):
		print("*", end="")
	for j in range(i-1):
		print("*", end="")
	print()

	
 *******
  *****
   ***
    *
>>> for i in range(1, 6):
	for j in range(5-i):
		print(" ", end="")
	for j in range(i):
		print("*", end="")
	for j in range(i-1):
		print("*", end="")
	print()

	
    *
   ***
  *****
 *******
*********
>>> for i in range(4, 0, -1):
	for j in range(5-i):
		print(" ", end="")
	for j in range(i):
		print("*", end="")
	for j in range(i-1):
		print("*", end="")
	print()

	
 *******
  *****
   ***
    *
>>>  movies = ["The Holy Grail", "The Life of Brian", "The Meaning of Life"]
 
SyntaxError: unexpected indent
>>> movies = ["The Holy Grail", "The Life of Brian", "The Meaning of Life"]
>>> movies.insert(1, 1975)
>>> movies
['The Holy Grail', 1975, 'The Life of Brian', 'The Meaning of Life']
>>> movies.insert(-1,1983)
>>> f
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    f
NameError: name 'f' is not defined
>>> movies
['The Holy Grail', 1975, 'The Life of Brian', 1983, 'The Meaning of Life']
>>> movies.append(1990)
>>> movies
['The Holy Grail', 1975, 'The Life of Brian', 1983, 'The Meaning of Life', 1990]
>>> movies.remove(1983)
>>> 
>>> 
>>> movies
['The Holy Grail', 1975, 'The Life of Brian', 'The Meaning of Life', 1990]
>>> movies.remove(1)
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    movies.remove(1)
ValueError: list.remove(x): x not in list
>>> movies.delete(1)
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    movies.delete(1)
AttributeError: 'list' object has no attribute 'delete'
>>> movies.delete(0)
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    movies.delete(0)
AttributeError: 'list' object has no attribute 'delete'
>>> del movies[1]
>>> movies
['The Holy Grail', 'The Life of Brian', 'The Meaning of Life', 1990]
>>> movies.delete(0)
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    movies.delete(0)
AttributeError: 'list' object has no attribute 'delete'
>>> for i in movies:
	print(i)

	
The Holy Grail
The Life of Brian
The Meaning of Life
1990
>>> movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
 ["Graham Chapman", ["Michael Palin", "John Cleese",
"Terry Gilliam", "Eric Idle", "Terry Jones"]]]
>>> for i in movies:
	print(i)

	
The Holy Grail
1975
Terry Jones & Terry Gilliam
91
['Graham Chapman', ['Michael Palin', 'John Cleese', 'Terry Gilliam', 'Eric Idle', 'Terry Jones']]
>>> for i in movies:
	print(i)
        for j in i:
		
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> for i in movies:
	print(i)
        for j in i:
	    print(j)
	    
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> for i in movies:
        for j in i:
	    print(j)
	    
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> for i in movies:
	for j in i:
		print(j)

		
T
h
e
 
H
o
l
y
 
G
r
a
i
l
Traceback (most recent call last):
  File "<pyshell#119>", line 2, in <module>
    for j in i:
TypeError: 'int' object is not iterable
>>> a= 20
>>> type(a)
<class 'int'>
>>> b = 'abc'
>>> type(b)
<class 'str'>
>>> c = 0.3
>>> type(c)
<class 'float'>
>>> type(movies)
<class 'list'>
>>> type(movies) == 'list'
False
>>> type(movies) is list
True
>>> type(a) is int
True
>>> type(a) is float
False
>>> for i in movies:
	if i is list:
		for j in i:
			if type(j) is list:
				for k in j:
					print(k)
			else:
				print(j)
	else:
		print(i)

		
The Holy Grail
1975
Terry Jones & Terry Gilliam
91
['Graham Chapman', ['Michael Palin', 'John Cleese', 'Terry Gilliam', 'Eric Idle', 'Terry Jones']]
>>> for i in movies:
	if type(i) is list:
		for j in i:
			if type(j) is list:
				for k in j:
					print(k)
			else:
				print(j)
	else:
		print(i)

		
The Holy Grail
1975
Terry Jones & Terry Gilliam
91
Graham Chapman
Michael Palin
John Cleese
Terry Gilliam
Eric Idle
Terry Jones
>>> movies
['The Holy Grail', 1975, 'Terry Jones & Terry Gilliam', 91, ['Graham Chapman', ['Michael Palin', 'John Cleese', 'Terry Gilliam', 'Eric Idle', 'Terry Jones']]]
>>> movies.index(Terry Gilliam)
SyntaxError: invalid syntax
>>> l = ['a', 'b', 'c']
>>> l.index(1)
Traceback (most recent call last):
  File "<pyshell#147>", line 1, in <module>
    l.index(1)
ValueError: 1 is not in list
>>> l[1]
'b'
>>>   l[4, l[2, l[4]]]
  
SyntaxError: unexpected indent
>>> l[1]
'b'
>>> movies[1]
1975
>>> movies[4]
['Graham Chapman', ['Michael Palin', 'John Cleese', 'Terry Gilliam', 'Eric Idle', 'Terry Jones']]
>>> movies[4,2]
Traceback (most recent call last):
  File "<pyshell#153>", line 1, in <module>
    movies[4,2]
TypeError: list indices must be integers or slices, not tuple
>>> movies[4][1][2]
'Terry Gilliam'
>>> names = ['Michael', 'Terry']
>>> isinstance(names, list)
True
>>> num_names = len(names)
>>> type(num_names)
<class 'int'>
>>> isinstance(num_names, int)
True
>>> isinstance(num_names, list)
False
>>> movies
['The Holy Grail', 1975, 'Terry Jones & Terry Gilliam', 91, ['Graham Chapman', ['Michael Palin', 'John Cleese', 'Terry Gilliam', 'Eric Idle', 'Terry Jones']]]
>>> for i in movies:
	if isinstance(i, list):
		print (i)

		
['Graham Chapman', ['Michael Palin', 'John Cleese', 'Terry Gilliam', 'Eric Idle', 'Terry Jones']]
>>> for i in movies:
	if isinstance(i, list):
		for j in i:			
			
			if isinstance(j, list):
				for k in j:
					print(k)
			else:
				print(j)
			
	
	else:
		print(i)

		
The Holy Grail
1975
Terry Jones & Terry Gilliam
91
Graham Chapman
Michael Palin
John Cleese
Terry Gilliam
Eric Idle
Terry Jones
>>> 