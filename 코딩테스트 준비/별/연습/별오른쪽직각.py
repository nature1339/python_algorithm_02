for i in range(5): #i 가 0부터 5직전인 4까지 반복
    for j in range(5-i-1): #첫째줄에 공백이 4개고 
        print(' ', end = ' ')          
    for j in range(i):    #별이 i줄마다 반복 가로로 
        print('*', end = ' ')
    print()       # 공백
   