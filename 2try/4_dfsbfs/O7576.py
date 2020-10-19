import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())
# M : x축, N : y축
tomato = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
date = [[-1]*M for _ in range(N)]
q=deque()
dx = [1,-1,0,0]
dy = [0,0,-1,1]
def bfs():
    ans = 0
    while q:
        y, x = q.popleft()
        ans = date[y][x]
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0<=ny<N and 0<=nx<M:
                if tomato[ny][nx]==0 and date[ny][nx]==-1:
                    tomato[ny][nx]=1
                    date[ny][nx]=date[y][x]+1
                    q.append([ny, nx])
    for y in range(N):
        for x in range(M):
            if tomato[y][x]==0:
                return -1
    return ans
for y in range(N):
    for x in range(M):
        if tomato[y][x]==1:
            date[y][x]=0
            q.append([y,x])
print(bfs())