Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
i
>>> a = [1,2,3,1,4,5,6,7,1]
>>> a.index(1) #1이어디있냐 0번째 3,8번째 있지만 첫번째인 0번째만 기준

0
>>> 
>>> a.index(8)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    a.index(8)
ValueError: 8 is not in list
>>> #index가 없을때 에러가 남
>>> a.count(1)
3
>>> a.count(8)
0
>>> a.remove(8)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    a.remove(8)
ValueError: list.remove(x): x not in list
>>> l = [1,2,3,4]
>>> a = l.pop()
>>> l
[1, 2, 3]
>>> a
4
>>> l
[1, 2, 3]
>>> min(l)
1
>>> max(l)
3
>>> 
