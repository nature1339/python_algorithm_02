n, l = map(int(input().split()))
pl = list(map(int(input().split()))) # 1 2 100 101
pl.sort()

t = 0
c = 0
for p in pl: # 1 2 100 101
    if t < p :
        c += 1
        t = p + l - 1

print(c)