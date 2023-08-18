a, b, c = map(int, input("").split())

if a == b and b == c and a == c:
    print(10000+a*1000)
# elif a == b and b == c or b == c and c == a:
#     print(1000+a*100)   
elif a == b or a == c:
    print(1000 + a * 100)
elif b == c:
    print(1000 + b * 100)
# elif a!=b and b!=c and a!=c:
#     print(c * 100)   
else:
    print(100 * max(a, b, c))