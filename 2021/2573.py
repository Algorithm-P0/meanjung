import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
# N세로 M가로
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dy = [-1,1,0,0]
dx = [0,0,1,-1]
def check(y, x, visited):
    q = deque()
    q.append([y,x])
    visited[y][x]=True
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<N and 0<=nx<M:
                if visited[ny][nx]==False and graph[ny][nx]!=0:
                    q.append([ny, nx])
                    visited[ny][nx]=True

def melt():
    temp = [[0]*M for _ in range(N)]
    for y in range(N):
        for x in range(M):
            if graph[y][x]!=0:
                cnt=0
                for i in range(4):
                    ny = y + dy[i]
                    nx = x + dx[i]
                    if graph[ny][nx]==0:
                        cnt+=1
                if graph[y][x]-cnt>0:
                    temp[y][x]=graph[y][x]-cnt
                else:
                    temp[y][x]=0
    return temp

year = 0
while True:
    visited = [[False]*M for _ in range(N)]
    cnt = 0
    for y in range(N):
        for x in range(M):
            if visited[y][x]==False and graph[y][x]!=0:
                check(y, x, visited)
                cnt+=1
    if cnt>=2:
        print(year)
        break
    elif cnt==0:
        print(0)
        break
    graph = melt()
    year+=1