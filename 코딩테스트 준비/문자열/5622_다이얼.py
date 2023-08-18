ndic = {'ABC':3,'DEF':4, 'GHI':5, 'JKL':6, 'MNO':7, 'PQRS':8, 'TUV':9, 'WXYZ':10  }
word= input()
seconds = 0
for letter in word:
    for key in ndic.keys():
        if letter in key:
            seconds += ndic[key]
print(seconds)