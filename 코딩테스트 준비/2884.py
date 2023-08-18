h, m = map(int,input("").split())


 
# if m < 45 and h == 0 or m < 45 and h != 0: # (분 단위가 45분 미만이면서 시간 단위가 자정일 경우) 또는 (분 단위가 45분 미만이면서 시간 단위가 자정이 아닐 경우)
if m < 45: 
    if h == 0:
        h = 23 
    else:
        h -= 1
    m += 60 

print(h, m-45)
    
        
#     print(h-1, m+60-45)
# elif m >+ 45:
#     print(h+1, m+60-45)    
# else:
#     h == 0
#     print(h+24, m+60-45)  
           

