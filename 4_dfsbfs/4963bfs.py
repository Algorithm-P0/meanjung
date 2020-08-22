# 통과
import sys
dx=[0,1,-1,0,1,1,-1,-1]
dy=[1,0,0,-1,1,-1,1,-1]

def bfs(x,y):
    q=[[x,y]]
    while q:
        p=q.pop(0)
        x=p[0]
        y=p[1]
        visited[y][x]=1
        for i in range(8):
            ly = y+dy[i]
            lx = x+dx[i]
            if 0<=lx<w and 0<=ly<h:
                if mmap[ly][lx]==1 and visited[ly][lx]==0 and [lx,ly] not in q:
                    q.append([lx,ly])

while True:
    w, h =map(int, sys.stdin.readline().split())
    if w==0 and h==0:
        break
    mmap=[list(map(int, sys.stdin.readline().split())) for _ in range(h)]
    visited=[[0]*w for _ in range(h)]
    cnt=0
    for x in range(w):
        for y in range(h):
            if mmap[y][x]==1 and visited[y][x]==0:
                cnt+=1
                bfs(x,y)
    print(cnt)