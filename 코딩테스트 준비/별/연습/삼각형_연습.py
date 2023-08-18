for i in range(7):   # i 가 0부터 7직전인 6까지 반복
    for j in range(7-i-1): #j 는 오른쪽 직각삼각형을 위해 왼쪽에 공간을 만듬, i=0이면 7-0-1 = 6개 공간
        print(' ', end=' ')
    for j in range(i+1):  # j는 별의갯수를 오른쪽으로 i=0이면 별하나, i=2이면 왼쪽에 별 2개 .. 
        # if i // 2 != 0:
            print('*', end=' ')    
    for j in range(i):       #이걸 잘 모르겠음
        # if i // 2 != 0:       
             print('*', end=' ')    
    print()    