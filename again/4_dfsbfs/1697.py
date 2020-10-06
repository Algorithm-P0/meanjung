# 왜 틀렸는지 알 수가 없다.
import sys
from collections import deque
N, K = map(int, sys.stdin.readline().split())
visited = [False]*100001
time = [0]*100001
q = deque()
q.append(N)
visited[N]=True
while q:
    p = q.popleft()
    if p == K:
        break
    for i in (p+1, p-1, 2*p):
        if 0<=i<=10000 and visited[i]==False:
            q.append(i)
            visited[i]=True
            time[i]=time[p]+1
print(time[K])

