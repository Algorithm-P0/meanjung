import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
q = deque()
for i in range(1, N+1):
    q.append(i)
poplist =list(map(int, sys.stdin.readline().split()))
count = 0
for i in poplist:
    if q.index(i)>len(q)-1-q.index(i):
        while q[0]!=i:
            q.appendleft(q.pop())
            count+=1
    else:
        while q[0]!=i:
            q.append(q.popleft())
            count+=1
    q.popleft()
print(count)