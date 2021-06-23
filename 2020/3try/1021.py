import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
pos = list(map(int, sys.stdin.readline().split()))
q = deque()
for i in range(1, N+1):
    q.append(i)
count = 0
for p in pos:
    if pos.index(p)>len(pos)-1-pos.index(p):
        while pos[0]!=p:
            pos.appendleft(pos.pop())
            count += 1
    else:
        while pos[0]!=p:
            pos.append(pos.popleft())
            count += 1
    pos.popleft()
print(count)