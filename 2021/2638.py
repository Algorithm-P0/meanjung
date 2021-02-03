import sys
from collections import deque
# 세로 가로
N, M = map(int, sys.stdin.readline().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))
dy = [-1,1,0,0]
dx = [0,0,-1,1]
def bfs():
    q = deque()
    q.append([0,0])
    visited = [[False]*M for _ in range(N)]
    visited[0][0]=True
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<N and 0<=nx<M and visited[ny][nx]==False:
                if graph[ny][nx]>=1:
                    graph[ny][nx]+=1
                else:
                    visited[ny][nx]=True
                    q.append([ny, nx])
time = 0
while True:
    bfs()
    cht = 0
    for y in range(N):
        for x in range(M):
            if graph[y][x]>=3:
                graph[y][x]=0
                cht=1#녹인 게 있다
            elif graph[y][x]==2:
                graph[y][x]=1
    if cht==1:
        time+=1
    else:
        #더 녹은 치즈가 없다
        break
print(time)