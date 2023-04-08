# 25206번
# rating = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
# grade = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0]
# total = 0 # 학점 총합을 담을 변수
# result = 0 # (학점 * 과목평점) 총합을 담을 변수
# for i in range(20): #20줄 입력
#     s, p, g = input().split()
#     #과목, 학점, 과목평점이 띄어쓰기로 구분되어 들어오므로 split을 사용해서 세 변수에 나눠 저장
#     p = float(p) #실수 자료형으로 바꿔줌 (사칙연산 위해)
#     if g != 'P' : # 등급이 P인 과목은 계산 안함
#         total += p
#         result += p * grade[rating.index(g)]
# print('%.6f'%(result / total))
# #result를 total로 나누면 평점이고, 소수점 아래 6자까지 출력하기 위해 '%.6f'%를 사용

# 2839번
# sugar = int(input())
# bag = 0
# while sugar >= 0 :
#     if sugar % 5 == 0:  # 5의 배수이면
#         bag += sugar // 5  # 5로 나눈 몫을 구해야 정수가 됨
#         print(bag)
#         break
#     sugar -= 3  
#     bag += 1  # 5의 배수가 될 때까지 설탕-3, 봉지+1
    
#     #5키로 봉지가 많아야 좋기 때문에
#     #설탕-3, 봉지+1을 하면서 5로 나눠지는지 본다.
# else:
#     print(-1)
# #while문의 조건이 거짓이 되는 순간 else문이 실행되는
# #while ~ else문이다. for ~ else도 가능하다.


# average_score = (standard_score(학점) * jihun_score(지훈학점)) //total_standard_score






total_g = 0
total_p = 0

dic = {"A+":4.5,"A0":4.0, "B+":3.5, "B0":3.0, "C+":2.5, "C0":2.0, "D+":1.5, "D0":1.0, "F":0.0}

for i in range(20):
    s, p, g = input().split()
    p = float(p) 
    if g == "p":        
        continue
    g = dic[g]
    total_g += p * g
    total_p += p
#    과목명, 학점 3.0, 점수 A+
#    점수 * 학점// 총학점
print(total_g//total_p)
    
  
  