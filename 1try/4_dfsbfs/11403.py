import sys
from collections import deque

N = int(sys.stdin.readline())
graph = []
for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))
res = [[0]*N for _ in range(N)]
def bfs(i):
    q = deque()
    q.append(i)
    visited = [False]*N
    while q:
        p = q.popleft()
        for j in range(N):
            if graph[p][j]==1 and visited[j]==False:
                q.append(j)
                res[p][j]=1
                res[i][j]=1
                visited[j]=True
for i in range(N):
    bfs(i)
for r in res:
    print(' '.join(map(str, r)))
