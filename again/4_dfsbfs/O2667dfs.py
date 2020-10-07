"""
# dfs 재귀
def dfs(y, x):
    global res
    res+=1
    visited[y][x]=True
    for dy, dx in [(1,0),(-1,0),(0,-1),(0,1)]:
        ly = y + dy
        lx = x + dx
        if 0<=ly<N and 0<=lx<N:
            if visited[ly][lx]==False and house[ly][lx]==1:
                dfs(ly, lx)
"""

# dfs 스택
def dfs(y, x):
    global res
    s = [[y,x]]
    visited[y][x]=True
    while s:
        y, x = s.pop()
        res+=1
        for dy, dx in [(1,0),(-1,0),(0,-1),(0,1)]:
            ly = y + dy
            lx = x + dx
            if 0<=ly<N and 0<=lx<N:
                if visited[ly][lx]==False and house[ly][lx]==1:
                    s.append([ly,lx])
                    visited[ly][lx]=True

import sys
N = int(sys.stdin.readline())
house = [list(map(int, map(str, sys.stdin.readline().strip()))) for _ in range(N)]
visited = [[False]*N for _ in range(N)]
cnt = 0
lst=[]
for i in range(N):
    for j in range(N):
        if visited[i][j]==False and house[i][j]==1:
            res=0
            dfs(i,j)
            lst.append(res)
            cnt+=1
print(cnt)
lst.sort()
for l in lst:
    print(l)