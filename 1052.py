n, k = map(int(input()).split())  # 3  1

i = 1
sum = 0
for i in range(n):
    # 1+1 = 2
    # 2 + 1 + 1= 4  ,  sum + 1 = 4
    sum = i + 1 # 1+1 = 2
    sum = sum + k # sum = 2 + 1
    print(min(k))  
    