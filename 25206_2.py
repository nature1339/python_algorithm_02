

total_g = 0
total_p = 0

dic = {"A+":4.5,"A0":4.0, "B+":3.5, "B0":3.0, "C+":2.5, "C0":2.0, "D+":1.5, "D0":1.0, "F":0.0}

for i in range(20):
    s, p, g = input().split()
    p = float(p) 
    if g == "P":        
        continue
    g = dic[g]
    total_g += p * g
    total_p += p
#    과목명, 학점 3.0, 점수 A+
#    점수 * 학점// 총학점
print(total_g/total_p)
    