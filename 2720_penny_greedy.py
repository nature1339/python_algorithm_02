
# n = int(input())
# coin = [0, 0, 0, 0] #쿼터(Quarter, $0.25)의 개수, 다임(Dime, $0.10)의 개수, 니켈(Nickel, $0.05)의 개수, 페니(Penny, $0.01

# for i in range(1, n+1):
#     coin.append(1)

# for i in range(5):
#     if coin(max) > 0:
#         print(coin(max))
# 3 -> 300 , 
l = [25, 10, 5 , 1]

n = int(input())
for _ in range(n):
    money = int(input())
    for i in l:
        print(money // i, end=' ')
        money = money % i