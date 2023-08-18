i = 0
i, j = 0, 4
n = 4
while i <= n:
    j = 0
    while j < n - i:
        # if(j > i):
        print(' ', end=' ')
        j+=1
        # else:
    j = 0
    while j < i + 1:
        print('*', end=' ')    
        j += 1
    i+=1        
    print()