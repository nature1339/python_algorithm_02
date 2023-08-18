# n = int(input())
# l =[]
# 틀린 예시
# for i in range(n): # n+1 하면 안됨 0부터 n의 직전이라 n만큼 반복된다.
#     s = int(input())
#     l.append(s)
# print(l)    

#ValueError: invalid literal for int() with base 10: '1 4 1 2 4 2 4 2 3 4 4'
# 유효하지 않은 문자
# input() 에는 문자가 입력됨, 엔터가 끝나는 지점에 종료
n = int(input())
l =[]    
l = list(map(int, input().split()))



count = 0
v = int(input())

for i in l:
    if v == i:      
        count += 1
print(count)
# if 가 false가 되면, print(count) 가 if 문안에있으면 print(count)가안되서 밖으로 뺌
#2   11번돌때
# 2 = i 와 같으면 count증가

# 1 4 1 2 4 2 4 2 3 4 4 요소와 같으면
        
    