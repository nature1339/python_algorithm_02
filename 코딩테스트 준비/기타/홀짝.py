Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> string = "홀짝홀짝홀짝"
>>> str(13)
'13'
>>> print(string[0],string[3], string[5])
홀 짝 짝
>>> print(string[0], string[2], string[4], end='')
홀 홀 홀
>>> print(string[0], string[2], string[4], sep='')
홀홀홀
>>> string[:]
'홀짝홀짝홀짝'
>>> sting[::2]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    sting[::2]
NameError: name 'sting' is not defined
>>> string[::2]
'홀홀홀'
>>> print(string[::2])
홀홀홀
>>> #023
>>> #END023
>>> url = "http://sharebook.kr"
>>> print(url)
http://sharebook.kr
>>> print(url[-1:-3])

>>> print(url[-1:-3:-1])
rk
>>> url[-2]
'k'
>>> url[-2:]
'kr'
>>> url[-2:-1]
'k'
>>> url[-2::-1]
'k.kooberahs//:ptth'
>>> l = ["http://sharebook.kr", "http://sharebook.com", "http://sharebook.test"]
>>> 
>>> 
>>> l
['http://sharebook.kr', 'http://sharebook.com', 'http://sharebook.test']
>>> for i in l:
	print(i.split('.'))

	
['http://sharebook', 'kr']
['http://sharebook', 'com']
['http://sharebook', 'test']
>>> for i in l:
	url = i.split('.')
	print(len(url))

	
2
2
2
>>> for i in l:
	url = i.split('.')
	length = len(url)

	
>>> 
>>> l = ["http://sharebook.kr", "http://admin.sharebook.com", "http://sharebook.test" ]
>>> for i in l:
	url = i.split('.')
	print(url)

	
['http://sharebook', 'kr']
['http://admin', 'sharebook', 'com']
['http://sharebook', 'test']
>>> l = ["http://www.sharebook.kr", "http://www.admin.sharebook.com", "http://www.sharebook.test" ]
>>> for i in l:
	url = i.split('.')
	print(url)
	
>>> 
>>> 
>>> 
>>> l = ["http://www.sharebook.kr", "http://www.admin.sharebook.com", "http://www.sharebook.test" ]
>>> for i in l:
	url = i.split('.')
	print(url)

	
['http://www', 'sharebook', 'kr']
['http://www', 'admin', 'sharebook', 'com']
['http://www', 'sharebook', 'test']
>>> for i in l:
	url = i.split(')
		      
SyntaxError: EOL while scanning string literal
>>> for i in l:
	url = i.split('.')
	print(url[len(url) - 1])

	
kr
com
test
>>> #END027
>>> 