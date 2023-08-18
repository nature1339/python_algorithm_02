Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
from collections import deque
queue = deque()
res = []
n, k = map(int, input().split())
7 3
n
7
k
k
3
n
7
k
3
for i in range(1, n + 1):
    queue.append(i)

    
queue
deque([1, 2, 3, 4, 5, 6, 7])
while queue:
    for i in range(k - 1):
        queue.append(queue.popLeft())
    res.append(queue.popLeft())
print('<', end='')
SyntaxError: invalid syntax
while queue:
    for i in range(k - 1):
        queue.append(queue.popLeft())
    res.append(queue.popLeft())

    
Traceback (most recent call last):
  File "<pyshell#18>", line 3, in <module>
    queue.append(queue.popLeft())
AttributeError: 'collections.deque' object has no attribute 'popLeft'. Did you mean: 'popleft'?
while queue:
    for i in range(k - 1):
        queue.append(queue.popleft())
    res.append(queue.popleft())

    
print('<', end='')
<
print('<' + ', '.join(res) + '>')
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    print('<' + ', '.join(res) + '>')
TypeError: sequence item 0: expected str instance, int found
res
[3, 6, 2, 7, 5, 1, 4]
print('<' + ', '.join(map(str, res)) + '>')
<3, 6, 2, 7, 5, 1, 4>
# while queue: --> queue 가 비어있지 않는동안에
#.join(map(str, res)) -> ,띄어쓰기로 res->str문자열로 바꾼후 , 띄어쓰기로 연결

from collections import deque
queue = deque()
res = []
n, k = map(int, input().split())

for i in range(1, n + 1):
    queue.append(i)

while queue:
    for i in range(k - 1):
        queue.append(queue.popleft())
    res.append(queue.popleft())
print('<' + ', '.join(map(str, res)) + '>')