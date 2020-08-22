def bfs(y, x):
    global count
    q=[[y,x]]
    while q:
        p=q.pop(0)
        y=p[0]
        x=p[1]
        visited[y][x]=1
        count+=1
        for i in range(4):
            lx = x+dx[i]
            ly = y+dy[i]
            if 0<=lx<N and 0<=ly<N:
                if house[ly][lx]==1 and visited[ly][lx]==0 and [ly,lx] not in q:
                    q.append([ly, lx])

import sys
N=int(sys.stdin.readline())
house=[]
dx=[0,1,-1,0]
dy=[1,0,0,-1]
for _ in range(N):
    h=sys.stdin.readline().strip()
    house.append(list(map(int, h)))
visited=[[0]*N for _ in range(N)]
ans=[]
for i in range(N):
    for j in range(N):
        if house[i][j]==1 and visited[i][j]==0:
            count=0
            bfs(i,j)
            ans.append(count)
ans.sort()
print(len(ans))
for a in ans:
    print(a)