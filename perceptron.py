
xl = [(0,0), (0, 1), (1, 0), (1, 1)]

for x in xl:
    def z(x):
        w1 = 0.1
        w2 = 0.7
        z = x*w1 + x*w2  
        return z
    print(z(x))
        


