for i in range(7):   # i 가 0부터 7직전인 6까지 반복
    for j in range(7-i-1): #j 는 오른쪽 직각삼각형을 위해 왼쪽에 공간을 만듬, i=0이면 7-0-1 = 6개 공간
        print(' ', end=' ')
    for j in range(i+1):  # j는 별의갯수를 오른쪽으로 i=0이면 별하나, i=2이면 왼쪽에 별 2개 .. 
        # if i // 2 != 0:
        print('*', end=' ')    
    for j in range(i):       #i가 맨첨에 6까지이니까 i= 6이면 삼각형 맨 마지막줄에 오른쪽이 별 6개라서 , i 가 6 일때 5부터 0이니까 별 6,  i가 5일때 별 5
        # if i // 2 != 0:       
        print('*', end=' ')    
    print()    
for i in range(5,-1,-1):    #삼각형을 뒤집는것. i가 5가 0이 되고, i가 1이 4가됨..... i를 5부터 0번째줄까지해야하니 -1까지이고 뒤로가니 -1
    for j in range(5-i+1): #j 는 오른쪽 직각삼각형을 위해 왼쪽에 공간을 만듬, i=0이면 5-0+1 = 6개 공간
        print(' ', end=' ')
    for j in range(i+1):  # j는 별의갯수를 오른쪽으로 i=0이면 별하나, i=2이면 왼쪽에 별 2개 .. 
        # if i // 2 != 0:
        print('*', end=' ')    
    for j in range(i):       #이걸 잘 모르겠음
        # if i // 2 != 0:       
        print('*', end=' ')    
    print()    