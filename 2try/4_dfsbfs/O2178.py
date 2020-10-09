import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
# 세로: N, 가로: M
miro = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
# 1: 지날 수 있음, 0: 지날 수 없음
visited = [[-1]*M for _ in range(N)]
dx = [1,-1,0,0]
dy = [0,0,-1,1]
d = deque()
d.append([0,0])
visited[0][0]=1
while d:
    y, x = d.pop()
    if y==N-1 and x==M-1:
        break
    for i in range(4):
        ly, lx = y + dy[i], x + dx[i]
        if 0<=ly<N and 0<=lx<M:
            if visited[ly][lx]==-1 and miro[ly][lx]==1:
                # y, x에 가까운 것들부터 먼저 pop하고
                # appendleft하여 나중에 pop되도록.
                d.appendleft([ly,lx])
                visited[ly][lx]=visited[y][x]+1
print(visited[-1][-1])
