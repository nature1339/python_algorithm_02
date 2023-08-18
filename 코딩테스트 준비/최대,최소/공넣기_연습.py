n, m = map(int, input().split())

l = [o, for i in range(n)]

for i in range(n):
    i, j, k = map(int, input().split())
    for t in range(i, j+1):
        l[t-1] = k

for i in range(n):
    print(l[i], end=' ')