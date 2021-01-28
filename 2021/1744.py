import sys
from collections import deque
N = int(sys.stdin.readline())
negative = []
positive = []
ans = 0
for _ in range(N):
    i =int(sys.stdin.readline())
    if i<=0:
        negative.append(i)
    elif i==1:
        ans+=1
    else:
        positive.append(i)
negative.sort()
positive.sort()

ndeque = deque(negative)
pdeque = deque(positive)
while ndeque:
    if len(ndeque)==1:
        ans += ndeque.pop()
        break
    x = ndeque.popleft()
    y = ndeque.popleft()
    ans += x*y
while pdeque:
    if len(pdeque)==1:
        ans += pdeque.pop()
        break
    x = pdeque.pop()
    y = pdeque.pop()
    ans += x*y
print(ans)