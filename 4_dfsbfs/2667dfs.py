def dfs(y, x):
    global count
    stack=[(x,y)]
    visited[y][x]=True
    count+=1
    for i in range(4):
        lx=x+dx[i]
        ly=y+dy[i]
        if 0<=lx<N and 0<=ly<N:
            if house[ly][lx]==1 and visited[ly][lx]==False:
                dfs(ly, lx)


import sys
N=int(sys.stdin.readline())
house=[]
for _ in range(N):
    h = sys.stdin.readline().strip()
    house.append(list(map(int, h)))
visited=[[False]*N for _ in range(N)]
dx=[1,-1,0,0]
dy=[0,0,1,-1]
ans=[]
for i in range(N):
    for j in range(N):
        count=0
        if house[i][j]==1 and visited[i][j]==False:
            dfs(i,j)
            ans.append(count)
ans.sort()
print(len(ans))
for a in ans:
    print(a)