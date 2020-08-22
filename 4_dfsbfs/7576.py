"""
q를 그냥 list로 구현하면 q.pop(0)을 실행할 때 시간복잡도가
O(n)이므로 시간초과.
deque를 사용해 q.popleft() -> 시간복잡도 : O(1)
"""
from collections import deque
import sys
M, N =map(int, sys.stdin.readline().split())
tomato=[list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited=[[0]*M for _ in range(N)]
ripen=[[0]*M for _ in range(N)]
dx=[0,1,0,-1]
dy=[1,0,-1,0]
q=deque()
for i in range(N):
    for j in range(M):
        if tomato[i][j]==1:
            q.append([i,j])
# N, i: 세로 // M, j: 가로
while q:
    p=q.popleft()
    y=p[0]
    x=p[1]
    visited[y][x]=1
    for i in range(4):
        ly=y+dy[i]
        lx=x+dx[i]
        if 0<=lx<M and 0<=ly<N:
            if tomato[ly][lx]==0 and visited[ly][lx]==0:
                tomato[ly][lx]=1
                ripen[ly][lx]=ripen[y][x]+1
                q.append([ly,lx])
if any(0 in x for x in tomato):
    print(-1)
else:
    print(max(map(max, ripen)))