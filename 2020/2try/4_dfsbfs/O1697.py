import sys
from collections import deque
N, K = map(int, sys.stdin.readline().split())
time = [-1]*100001
q = deque()
q.append(N)
time[N]=0
while q:
    p = q.popleft()
    if p == K:
        break
    for i in (p+1, p-1, 2*p):
        if 0<=i<=100000 and time[i]==-1:
            q.append(i)
            time[i]=time[p]+1
print(time[K])

