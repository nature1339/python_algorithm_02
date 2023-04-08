s = int(input())
b = 0
while s >= 0:
    if (s % 5 == 0):
        b = b + s // 5
        s = 0
        print(b)
        break
    s = s - 3
    b = b + 1
if (s != 0):
    print(-1)