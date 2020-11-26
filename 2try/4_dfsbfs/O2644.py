import sys
from collections import deque

n = int(sys.stdin.readline())
a, b = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline()) # 부모 자식간의 관계의 수
graph = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x][y]=1
    graph[y][x]=1
visited = [-1]*(n+1)
visited[a]=0
# a -> b
q=deque()
q.append(a)
while q:
    p = q.popleft()
    for i in range(1, n+1):
        if graph[p][i]==1 and visited[i]==-1:
            visited[i]=visited[p]+1
            if i==b:
                print(visited[i])
                sys.exit()
            else:
                q.append(i)
print(-1)

