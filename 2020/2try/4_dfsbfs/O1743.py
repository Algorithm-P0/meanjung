import sys
from collections import deque

N, M, K = map(int, sys.stdin.readline().split())
# 세로 : N, 가로 : M
graph = [[0]*(M+1) for _ in range(N+1)]
visited = [[False]*(M+1) for _ in range(N+1)]
for _ in range(K):
    r, c = map(int, sys.stdin.readline().split())
    graph[r][c]=1
dy = [1,-1,0,0]
dx = [0,0,1,-1]
res = []
def bfs(y, x):
    q = deque()
    q.append([y, x])
    visited[y][x]=True
    cnt=0
    while q:
        y, x = q.popleft()
        cnt+=1
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 1<=ny<=N and 1<=nx<=M:
                if graph[ny][nx]==1 and visited[ny][nx]==False and [ny, nx] not in q:
                    q.append([ny, nx])
                    visited[ny][nx]=True
    return cnt
for y in range(1, N+1):
    for x in range(1, M+1):
        if visited[y][x]==False and graph[y][x]==1:
            res.append(bfs(y,x))
print(max(res))