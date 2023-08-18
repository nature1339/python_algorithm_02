n, m =map(int, input().split())
# l = list(map(int, input().split()))

# l = [ 1 , 2, 1, 1]
l =[0 for _ in range(n)] # 바구니개수만큼 0으로 초기화한다
for _ in range(m):
    i, j, k = map(int, input().split())
    for t in range(i, j+1):      
        l[t-1]=k

for i in range(n):
    print(l[i], end=' ')   
    # l[1] = 3
    # l[2] = 3
    # l[3] = 4
    # l[4] = 4
    # l[1] = 1
    # l[4] = 1
    # l[2] = 2
    # l[5] = 0
    
    
    
    
    
        
    # n[i-1]=k
    # l.append(k)