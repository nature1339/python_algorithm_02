sugar = int(input())
bag = 0
while sugar >= 0 :
    if sugar % 5 == 0:  # 5의 배수이면
        bag += sugar // 5  # 5로 나눈 몫을 구해야 정수가 됨
        print(bag)
        break
    sugar -= 3  
    bag += 1  # 5의 배수가 될 때까지 설탕-3, 봉지+1
    
    #5키로 봉지가 많아야 좋기 때문에
    #설탕-3, 봉지+1을 하면서 5로 나눠지는지 본다.
else:
    print(-1)
#while문의 조건이 거짓이 되는 순간 else문이 실행되는
#while ~ else문이다. for ~ else도 가능하다.



# n = int(input())

# a = n // 5
# b = 

# for i in range():
#     if n == 5 * a + 3 * b :
#         print( 
    
#     else: 
       


# else:
#      print("-1") #""하던말던 상관없음


