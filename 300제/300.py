Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # 001
>>> print("Hello World")
Hello World
>>> # 001 END
>>> # 002 START
>>> print("Mary's cosmetics")
Mary's cosmetics
>>> print('Mary\'s cosmetics')
Mary's cosmetics
>>> print("Mary\"s cosmetics")
Mary"s cosmetics
>>> print("신씨가 소리질렀다. \"도둑이야".")
      
SyntaxError: EOL while scanning string literal
>>> print("신씨가 소리질렀다. \"도둑이야\".)
      
SyntaxError: EOL while scanning string literal
>>> print("신씨가 소리질렀다.\ "도둑이야\".\")
SyntaxError: invalid escape sequence \ 
>>> print("신씨가 소리질렀다.\"도둑이야\".)
      
SyntaxError: EOL while scanning string literal
>>> print("신씨가 소리질렀다.\"도둑이야\.")
신씨가 소리질렀다."도둑이야\.
>>> print("신씨가 소리질렀다.\"도둑이야.")
신씨가 소리질렀다."도둑이야.
>>> print("신씨가 소리질렀다.\"도둑이야.\"")
신씨가 소리질렀다."도둑이야."
>>> 
>>> # 002 END
>>> # 003 END
>>> #004start
>>> print("\"C:\Windows\"")
"C:\Windows"
>>> # 004 END
>>> #005start
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> print("안녕하세요.\n만나서\t\t반갑습니다.")
안녕하세요.
만나서		반갑습니다.
>>> # 005 END
>>> print ("오늘은", "일요일")
오늘은 일요일
>>> # 006 END
>>> print("naver;kakao;sk;samsung")
naver;kakao;sk;samsung
>>> print("naver", "kakao", "samsung", sep=";")

naver;kakao;samsung
>>> print("naver", "kakao", "samsung", sep="-")
naver-kakao-samsung
>>> # 007 END
>>> print(naver,kakao,sk,samsung, sep="/")
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    print(naver,kakao,sk,samsung, sep="/")
NameError: name 'naver' is not defined
>>> print("naver","kakao","sk","samsung", sep="/")
naver/kakao/sk/samsung
>>> # 008 END
>>> print("first/n, second")
first/n, second
>>> print("first");print("second")
first
second
>>> print("first", end='');print("second")
firstsecond
>>> print("first", end='+');print("second")
first+second
>>> # 009 END
>>> print("9/3")
9/3
>>> print(9/3)
3.0
>>> print(5/3)
1.6666666666666667
>>> # 010 END
>>> 삼성전자 = 50000
>>> print(삼성전자*10)
500000
>>> # 011 END
>>> 시가총액=298조
SyntaxError: invalid syntax
>>> 
    현재가=50,000원
PER	15.79
SyntaxError: unexpected indent
>>> 시가총액=298
>>> 현재가=50,000
>>> PER=15.79
>>> # 012 END
>>> s = "hello"
>>> t = "python"
>>> print(s+" "+t)
hello python
>>> print(s, t, sep=' ')
hello python
>>> print(s, t)
hello python
>>> # 013 END
>>> print(2 + 2 * 3)
8
>>> # 014 END
>>>  #015 END
>>> num_str = int("720")
>>> print(num_str)
720
>>> #016 END
>>> string(num_str)
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    string(num_str)
NameError: name 'string' is not defined
>>> str(num_str)
'720'
>>> #016, 017 END
>>> float("15.79")
15.79
>>> #018 END
>>> year = int("2020")
>>> print(year,year-1,year-2))
SyntaxError: unmatched ')'
>>> print(year,year-1,year-2)
2020 2019 2018
>>> #019 END
>>> print(48,584*10)
48 5840
>>> print(48584*10)
485840
>>> #020 END
>>> letters = 'python'
>>> str(letters)
'python'
>>> print(letters[0],letters[2])
p t
>>> #021 END
>>> license_plate = "24가 2210"
>>> print(license_plate [-1:-5])

>>> print(license_plate [5:8])
210
>>> license_place[-1:-5:-1]
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    license_place[-1:-5:-1]
NameError: name 'license_place' is not defined
>>> license_plate[-1:-5:-1]
'0122'
>>> int(license_plate[-1:-5:-1])
122
>>> int(license_plate[5:])
210
>>> icense_plate[5:]
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    icense_plate[5:]
NameError: name 'icense_plate' is not defined
>>> license_plate[5:]
'210'
>>> license_plate
'24가 2210'
>>> license_plate[5:-1]
'21'
>>> license_plate[5:]
'210'
>>> license_plate[4:]
'2210'
>>> license_plate[-4:]
'2210'
>>>  #022 END
>>> 