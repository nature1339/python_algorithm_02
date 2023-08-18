word = input()

dic = {"ABC": 3, "DEF": 4, "GHI": 5, "JKL": 6, "MNO": 7, "PQR": 8, "STU": 9, "VWZ": 10}

seconds = 0

for letter in word:
    for key in dic.keys():
        if letter in key:
            seconds = seconds + dic[key]
print(seconds)              
    
