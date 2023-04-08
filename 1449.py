n, l = map(int, input().split())
pl = list(map(int, input().split()))
pl.sort()

t = 0
c = 0

for p in pl: 
    if t < p:  
        c += 1
        t = p+l-1

print(c)        
        