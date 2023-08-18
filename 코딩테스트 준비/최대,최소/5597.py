l = []
for _ in range(28):
    l.append(int(input()))
for i in range(30):
    if i+1 not in l:
        print(i+1)

#     l = []        
# for i in range(28):
#     n = int(input())
#     for i in range(28):
#         l.append(i)
#         if i not in l:
#            print(i)

# l = [i + 1 for i in range(30)]
# for i in range(28):
#     l.remove(int(input()))
# for i in l:
#     print(i)