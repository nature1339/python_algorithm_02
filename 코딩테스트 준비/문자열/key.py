Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=  "010-1234-5678"
>>> a.split("-")
['010', '1234', '5678']
>>> b = "010 1234 5678"
>>> b.split(" ")
['010', '1234', '5678']
>>> b = " 010 1234 5678 "
>>> b.split(" ")
['', '010', '1234', '5678', '']
>>> b.strip()
'010 1234 5678'
>>> len(b)
15
>>> 
>>> l = b.split(" ")
>>> 
>>> len(b)
15
>>> len(l)
5
>>> l = b.strip()
>>> 
>>> 
>>> a = '789'
>>> a[::-1]
'987'
>>> d = {
	: 'one', 2: 'two', '1': 'str one'}
SyntaxError: invalid syntax
>>> d = {1: 'one', 2: 'two', '1': 'str one'}
>>> d
{1: 'one', 2: 'two', '1': 'str one'}
>>> d[1] = 'eleven'
>>> d
{1: 'eleven', 2: 'two', '1': 'str one'}
>>> d['1']
'str one'
>>> d['1'] ='eleven'
>>> 
>>> d
{1: 'eleven', 2: 'two', '1': 'eleven'}
>>> d[3] = 'three'
>>> d
{1: 'eleven', 2: 'two', '1': 'eleven', 3: 'three'}
>>> d.keys()
dict_keys([1, 2, '1', 3])
>>> list(d.keys())
[1, 2, '1', 3]
>>> W = "WA"
>>> for w in W:
	print(w)

	
W
A
>>> 