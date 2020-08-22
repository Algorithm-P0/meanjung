import sys

N, M=map(int, sys.stdin.readline().split())
maze=[]
dx=[0,1,0,-1]
dy=[1,0,-1,0]
visited=[[0]*M for _ in range(N)]
dist=[[0]*M for _ in range(N)]
for _ in range(N):
    c=sys.stdin.readline().strip()
    maze.append(list(map(int, c)))

q=[[0,0]]
dist[0][0]=1
while q:
    y, x = q.pop(0)
    visited[y][x]=1
    for i in range(4):
        ly=y+dy[i]
        lx=x+dx[i]
        if 0<=lx<M and 0<=ly<N:
            if visited[ly][lx]==0 and maze[ly][lx]==1 and [ly,lx] not in q:
                q.append([ly,lx])
                dist[ly][lx]=dist[y][x]+1

print(dist[-1][-1])