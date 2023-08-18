for i in range(6):
    for j in range(6-i):
        print(' ', end ="")
    for j in range(i*2+1):
        print('*', end="")    
    print()