word = input()

dict = { "ABC": 3, "DEF": 4, "GHI": 5, "JKL": 6, "MNO": 7, "PQRS": 8, "TUV": 9, "WXYZ": 10 }

seconds = 0

for letter in word :
    for key in dict.keys():
        if letter in key:
           seconds += dict[key]
print(seconds)           