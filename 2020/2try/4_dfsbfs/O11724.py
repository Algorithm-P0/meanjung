import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
visited = [False]*(N+1)
def bfs(s):
    visited[s]=True
    q = deque()
    q.append(s)
    while q:
        x = q.popleft()
        for i in graph[x]:
            if visited[i]==False:
                q.append(i)
                visited[i]=True
cnt = 0
for i in range(1, N+1):
    if visited[i]==False:
        bfs(i)
        cnt+=1
print(cnt)
