n, m = map(int, input().split())

l = [i+1 for i in range(n)]

for i in range(m):
    i, j = map(int, input().split())
    t = l[i - 1]
    l[i-1] = l[j - 1]
    l[j-1] = t
  

for i in range(n):
    print(l[i], end=' ')            
    