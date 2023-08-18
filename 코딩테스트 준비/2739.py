n = int(input())

for i in range(1,10):  
    print(f'{n}*{i}={n*i}')
    # print('%d %s %f' % (3, "hi", 3.5))  # 정수, 문자열, 실수, 순서대로 들어감
    # print('{0} {1} {0} {2}'.format(1, 'hi', '3')) # 배열순, 리스트처럼 요소
    # print(f'{8} x {3} = {8*3}')