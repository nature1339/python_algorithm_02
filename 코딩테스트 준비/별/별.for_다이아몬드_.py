

for i in range(8):    
    for j in range(8 - i):
        print(' ', end='')
    for j in range(i * 2 + 1):
        print('*', end="")
    print()          
for i in range(6,-1,-1): #6부터 0까지
    for j in range(8 - i):
        print(' ', end='')
    for j in range(i * 2 + 1):
        print('*', end="")
    print()       