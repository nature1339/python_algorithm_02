n = int(input())

for _ in range(n):
    s = input()
    
    # print(s[0][-1]) # [9,2,1]  # 리스트, 문자열, 문자열은 " ", 숫자는 배열은아님[-1]안됨
    print(s[0]+s[-1])
    