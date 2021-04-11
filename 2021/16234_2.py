import sys
from collections import deque

N, L, R = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dy = [-1,1,0,0]
dx = [0,0,1,-1]
def bfs(y, x):
    q = deque()
    q.append([y, x])
    l = [[y,x]]
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<N and 0<=nx<N:
                if visited[ny][nx]==False and L<=abs(A[ny][nx]-A[y][x])<=R:
                    q.append([ny, nx])
                    visited[ny][nx]=True
                    l.append([ny, nx])
    return l
    

ans = 0
while True:
    to_break = 0
    visited = [[False]*N for _ in range(N)]
    for y in range(N):
        for x in range(N):
            if visited[y][x]==False:
                visited[y][x]=True
                temp = bfs(y, x)
                if len(temp)>=2:
                    to_break = 1
                    num = sum(A[ly][lx] for ly, lx in temp)//len(temp)
                    for ly, lx in temp:
                        A[ly][lx]=num
    if to_break==0:
        break
    ans+=1
                
print(ans)

    
