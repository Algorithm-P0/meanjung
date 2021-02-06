import sys
from collections import deque
N, L, R = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dy = [-1,1,0,0]
dx = [0,0,-1,1]
cnt = 0

def bfs(y, x):
    q = deque()
    q.append([y, x])
    temp = []
    temp.append([y, x])
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<N and 0<=nx<N and visited[ny][nx]==0:
                if L<=abs(A[y][x]-A[ny][nx])<=R:
                    visited[ny][nx]=1
                    q.append([ny, nx])
                    temp.append([ny, nx])
    return temp

while True:
    visited = [[0]*N for _ in range(N)]
    flag = False
    for y in range(N):
        for x in range(N):
            if visited[y][x]==0:
                visited[y][x]=1
                temp = bfs(y, x)
                if len(temp)>=2:
                    flag=True
                    num = sum([A[ly][lx] for ly, lx in temp])//len(temp)
                    for ly, lx in temp:
                        A[ly][lx]=num
    if flag==False:
        break
    cnt+=1
print(cnt)