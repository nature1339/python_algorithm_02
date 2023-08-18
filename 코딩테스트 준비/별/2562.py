
l =[]
for i in range(9):  # 숫자가 9개의 다른자연수 , range(n)이면 n만큼 반복
    n = int(input())
    l.append(n)
print(max(l))    
print(l.index(max(l))+1)  #컴퓨터가 아닌 사람눈으로 몇번채인지세야. 