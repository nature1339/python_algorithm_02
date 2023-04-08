t = int(input())


for _ in range(t):
    n = int(input())
    sl = list(map(int,input().split()))  # 3 5 9
    m = 0
    r = 0
#    sl.sort()  주가가 변동성이 있기때문

    for s in sl[-1::-1]:
        if m < s:
            m = s  #  s 가 최대 주가 기준이 됨
        elif s < m:
            r += m - s
        
    print(r)









    # for j in range(len(sl), -1, -1):
    #     if m < sl[j]:
    #         m = sl[j]
    #     elif m > sl[j]:
    #         r += m - sl[j]
    # print(r)
