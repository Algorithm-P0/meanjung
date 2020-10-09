# 알고스팟
import sys
from collections import deque

M, N =map(int, sys.stdin.readline().split())
miro=[list(map(int, map(str, sys.stdin.readline().strip()))) for _ in range(N)]
dist=[[-1]*M for _ in range(N)]
dist[0][0]=0
q=deque()
dx=[1,-1,0,0]
dy=[0,0,-1,1]
q.append([0,0])
while q:
    p=q.popleft()
    for i in range(4):
        lx=p[0]+dx[i]
        ly=p[1]+dy[i]
        if 0<=lx<N and 0<=ly<M:
            if dist[lx][ly]==-1:
                if miro[lx][ly]==0:
                    q.appendleft([lx,ly])#여기가 키포인트
                    dist[lx][ly]=dist[p[0]][p[1]]+0
                else:
                    q.append([lx,ly])
                    dist[lx][ly]=dist[p[0]][p[1]]+1
print(dist[-1][-1])
