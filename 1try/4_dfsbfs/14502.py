from collections import deque
import sys
N, M = map(int, sys.stdin.readline().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))
dy = [0,0,-1,1]
dx = [1,-1,0,0]
max_result = 0
def bfs():
    global max_result
    copy = [[0]*M for _ in range(N)]
    for y in range(N):
        for x in range(M):
            copy[y][x] = graph[y][x]
    result = 0
    arr = deque()
    for y in range(N):
        for x in range(M):
            if copy[y][x]==2:
                arr.append([y, x])
    while arr:
        y, x = arr.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<N and 0<=nx<M:
                if copy[ny][nx]==0:
                    copy[ny][nx]=2
                    arr.append([ny, nx])
    for i in copy:
        for j in i:
            if j==0:
                result+=1
    max_result = max(max_result, result)

def wall(cnt):
    if cnt==3:
        bfs()
        return
    for y in range(N):
        for x in range(M):
            if graph[y][x]==0:
                graph[y][x]=1
                wall(cnt+1)
                graph[y][x]=0

wall(0)
print(max_result)