import sys
from collections import deque
def solve(i):
    q = deque()
    q.append(i)
    visited[i]=True
    while q:
        p = q.popleft()
        x = P[p]
        if visited[x]==False:
            visited[x]=True
            q.append(x)
    return

t = int(sys.stdin.readline())
for _ in range(t):
    N = int(sys.stdin.readline())
    P = [0]
    P.extend(list(map(int, sys.stdin.readline().split())))
    visited = [False]*(N+1)
    count=0
    for i in range(1, N+1):
        if visited[i]==False:
            solve(i)
            count+=1
    print(count)

