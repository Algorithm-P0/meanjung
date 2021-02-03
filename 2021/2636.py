import sys
from collections import deque
# 세로 가로
N, M = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dy = [1,-1,0,0]
dx = [0,0,-1,1]


def bfs():
    q = deque()
    visited = [[False]*M for _ in range(N)]
    visited[0][0]=True
    q.append([0,0])
    cnt = 0
    while q:
        y, x= q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<N and 0<=nx<M and visited[ny][nx]==False:
                if graph[ny][nx]==1:
                    graph[ny][nx]=2
                    cnt+=1
                    visited[ny][nx]=True
                elif graph[ny][nx]==2:
                    continue
                elif graph[ny][nx]==0:
                    q.append([ny, nx])
                    visited[ny][nx]=True
    return cnt

def arrange():
    for y in range(N):
        for x in range(M):
            if graph[y][x]==2:
                graph[y][x]=0
time=0
res = 0
while True:
    c = bfs()
    if c==0:
        break
    arrange()
    time+=1
    res = c
print(time)
print(res)

