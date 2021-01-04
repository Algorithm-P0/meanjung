import sys
from collections import deque
#    위 오 아래 왼
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
H, W = map(int, sys.stdin.readline().split())
graph = []
for _ in range(H):
    graph.append(list(map(int, sys.stdin.readline().split())))

left = 0
for y in range(H):
    for x in range(W):
        if graph[y][x]==1:
            left+=1
def bfs(left):
    while q:
        now = q.popleft()
        for i in range(4):
            ny = now[0]+dy[i]
            nx = now[1]+dx[i]
            if 0<=ny<H and 0<=nx<W and visited[ny][nx]==0:
                visited[ny][nx]=1
                if graph[ny][nx]==1:
                    graph[ny][nx]=2
                    left-=1
                else:
                    q.append([ny, nx])
    return left

def delete():
    for y in range(H):
        for x in range(W):
            if graph[y][x]==2:
                graph[y][x]=0

q = deque()
count = 0
temp = left
while left!=0:
    visited = [[0]*W for _ in range(H)]
    q.append([0,0])
    visited[0][0]=1
    left = bfs(left)
    if left!=0:
        temp = left
    count+=1
    delete()

print(count)
print(temp)
