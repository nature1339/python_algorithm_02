Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 3 / 5
0.6
>>> 3//5
0
>>> 3 % 5
3
>>> '\t'
'\t'
>>> print('\t')
	
>>> print('\'')
'
>>> print("\"")
"
>>> print(1,2,3,5)
1 2 3 5
>>> print(1,2,3,5, sub='--')
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print(1,2,3,5, sub='--')
TypeError: 'sub' is an invalid keyword argument for print()
>>> print(1,2,3,5, sep='--')
1--2--3--5
>>> print(3, end='\n')
3
>>> print(3)
3
>>> print(3, end='')
3
>>> l = list(range(10))
>>> for i in l:
	print(i, end='\n')

	
0
1
2
3
4
5
6
7
8
9
>>> for i in l:
	print(i, end='')

	
0123456789
>>> 'df '  + 'sf '
'df sf '
>>> age = 30
>>> 'age: 30'
'age: 30'
>>> print(age)
30
>>> print("age:30")
age:30
>>> print(f."age:"age)
SyntaxError: invalid syntax
>>> print(f'age: {age}')
age: 30
>>> print('age: {0}'.format(age))
age: 30
>>> print('age: %d' % (age))
age: 30
>>> name = 'Steve'
>>> print(f'age: {age}, name: {name}')
age: 30, name: Steve
>>> print('age: {0}, name: {1}'.format(age, name))
age: 30, name: Steve
>>> print('age: {1}, name: {0}'.format(age, name))
age: Steve, name: 30
>>> print('age: {1}, name: {1}'.format(age, name))
age: Steve, name: Steve
>>> print('age: %d, name: %s' % (age, name))
age: 30, name: Steve
>>> print('age: ' + ', name: ' + name)
age: , name: Steve
>>> print('age: ' +
      + ', name: ' + name)
Traceback (most recent call last):
  File "<pyshell#35>", line 2, in <module>
    + ', name: ' + name)
TypeError: bad operand type for unary +: 'str'
>>> print('age: ' + str(age) + ', name: ' + name)
age: 30, name: Steve
>>> ## 문자열 출력 END
>>> 
>>> 
>>> text = '바이너리 데이터 레코드 배치 작업'
>>> print(text[0])
바
>>> print(text[0:4])
바이너리
>>> print(text[:4])
바이너리
>>> print(text[1])
이
>>> print(text[5:8])
데이터
>>> print(text[-2:])
작업
>>> print(text[-5:-4)
      
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
>>> print(text[-5:-4])
배
>>> print(text[-5:-3])
배치
>>> print(text[0::1])
바이너리 데이터 레코드 배치 작업
>>> print(text[::2])
바너 이 코 치작
>>> print(text[-1::2])
업
>>> print(text[-1:2])

>>> # [종료 지점]
>>> # [종료 익덱트 직전까지]]
>>> # [시작 인덱스:종료 익덱트 직전까지]
>>> # [종료 익덱트 직전까지] -> 0부터 시작 (종료는 5일 경우 4까지)
>>> # [시작 인덱스:종료 인덱트 직전까지]
>>> # [:종료 인덱트 직전까지] -> 0부터 시작하여 ~~
>>> # [:] -> 처음부터 끝까지
>>> # [시작 인덱스:종료 익덱트 직전까지:스태핑] -> 스태핑: 마이너스일 경우 역방향, 플러스일 경우 정방향
>>> # 디폴트 값 (생략 시엔 1)
>>> # [시작 인덱스::-1] -> 시작 인덱스부터 처음까지 1칸씩
>>> # [시작 인덱스::-2] -> 시작 인덱스부터 처음까지 2칸씩
>>> # [시작 인덱스::2] -> 시작 인덱스부터 마지막까지 2칸씩
>>> # [:종료 인덱스 직전까지:2] -> 처음부터 종료 인덱스 직전까지 2칸씩
>>> print([-1:3])print(text[-1:2])
SyntaxError: invalid syntax
>>> print(text[-2:])
작업
>>> # 슬라이싱
>>> 
>>> 
>>> text.split()
['바이너리', '데이터', '레코드', '배치', '작업']
>>> text_list = text.split()
>>> text_list[-1]
'작업'
>>> print(text[-1])
업
>>> print(text_list[-1])
작업
>>> 