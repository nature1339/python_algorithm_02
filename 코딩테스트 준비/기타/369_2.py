i = 0
j = 1

while i < 9: 
    i += 3
    # if i % 3 != 0:
    #     continue
    j = 1
    while j <= 9:
        print(f'{i}*{j}={i * j}')
        j += 1
        