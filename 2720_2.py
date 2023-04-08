
n = int(input())
l = [25, 10, 5, 1]

for _ in range(n):  #25, 10, 5, 1
    moeny = int(input())
    for i in l:        
        print(money // i, end = " ")
        money = money % i #124 // 25 = ~ 개