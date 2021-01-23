import sys
from collections import deque
N = int(sys.stdin.readline())#보드의 크기
K = int(sys.stdin.readline())#사과 개수
graph = [[0]*N for _ in range(N)]
for _ in range(K):
    y, x = map(int, sys.stdin.readline().split())
    graph[y-1][x-1]=1
L = int(sys.stdin.readline())
times={}
for _ in range(L):
    X, C = map(str, sys.stdin.readline().split())
    times[int(X)]=C
#    상 우 하 좌
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

y, x = 0, 0
direction = 1
visited = deque([[y,x]])
graph[y][x]=2
time=1
def change(direction, C):
    if C=='L':
        direction = (direction+3)%4
    else:
        direction = (direction+1)%4
    return direction

while True:
    y+=dy[direction]
    x+=dx[direction]
    if 0<=y<N and 0<=x<N and graph[y][x]!=2:
        if graph[y][x]!=1:
            ny, nx = visited.popleft()
            graph[ny][nx]=0
        visited.append([y,x])
        graph[y][x]=2
        if time in times.keys():
            direction = change(direction, times[time])
        time+=1
    else:
        break
print(time)