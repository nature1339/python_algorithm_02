h,m = map(int, input().split())
a = int(input())

h2 = a // 60
m2 = a % 60

if m+m2 >= 60:
    h2 += 1
    m = m2+m -60
else:
    m = m+m2
h = (h + h2)%24

print(h, m)    


