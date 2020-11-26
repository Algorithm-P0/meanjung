import sys
from collections import deque
N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
graph = [[0]*N for _ in range(N)]
for _ in range(K):
    y, x = map(int, sys.stdin.readline().split())
    graph[y-1][x-1]=1
L = int(sys.stdin.readline())
times = {}
for _ in range(L):
    x, c = map(str, sys.stdin.readline().strip().split())
    times[int(x)]=c
#    하(0) 우(1)  상(2)  좌(3)
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
def change(d, c):
    if c=='L':
        d = (d-1)%4
    else:
        d = (d+1)%4
    return d

def start():
    y, x = 0, 0
    direction = 1
    visited = deque([[y, x]])
    graph[y][x]=2
    time=1
    while True:
        y = y + dy[direction]
        x = x + dx[direction]
        if 0<=y<N and 0<=x<N and graph[y][x]!=2:
            if graph[y][x]!=1:#사과가 없다면
                ny, nx = visited.popleft()
                graph[ny][nx]=0
            visited.append([y, x])
            graph[y][x]=2
            if time in times.keys():
                direction = change(direction, times[time])
            time+=1
        else:
            return time
print(start())

