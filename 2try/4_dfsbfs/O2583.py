# M : 세로, N : 가로, K : 직사각형 개수
import sys
from collections import deque

M, N, K = map(int, sys.stdin.readline().split())
graph = [[0]*(N) for _ in range(M)]
for _ in range(K):
    lx, ly, rx, ry = map(int, sys.stdin.readline().split())
    for y in range(ly, ry):
        for x in range(lx, rx):
            graph[y][x]=1
res = []
dy = [1,-1,0,0]
dx = [0,0,1,-1]
visited = [[False]*(N) for _ in range(M)]
def bfs(y, x):
    q = deque()
    q.append([y, x])
    visited[y][x]=True
    cnt = 0
    while q:
        y, x = q.popleft()
        cnt+=1
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0<=ny<M and 0<=nx<N:
                if graph[ny][nx]==0 and visited[ny][nx]==False and [ny,nx] not in q:
                    q.append([ny,nx])
                    visited[ny][nx]=True
    res.append(cnt)
for y in range(M):
    for x in range(N):
        if graph[y][x]==0 and visited[y][x]==False:
            bfs(y, x)
print(len(res))
res.sort()
print(' '.join(map(str, res)))