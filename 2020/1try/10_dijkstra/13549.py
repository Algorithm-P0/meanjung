import sys
from collections import deque
N, K = map(int, sys.stdin.readline().split())
time = [-1]*100001
time[N]=0
q=deque()
q.append(N)
while q:
    p = q.popleft()
    if p==K:
        break
    if 0<=2*p<100001 and time[2*p]==-1:
        q.appendleft(2*p)
        time[2*p]=time[p]
    if 0<=p-1<100001 and time[p-1]==-1:
        q.append(p-1)
        time[p-1]=time[p]+1
    if 0<=p+1<100001 and time[p+1]==-1:
        q.append(p+1)
        time[p+1]=time[p]+1
print(time[K])