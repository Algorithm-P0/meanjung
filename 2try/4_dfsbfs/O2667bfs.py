import sys
from collections import deque
N = int(sys.stdin.readline())
house = [list(map(int, map(str, sys.stdin.readline().strip()))) for _ in range(N)]
discovered = [[False]*N for _ in range(N)]
dx = [1,-1,0,0]
dy = [0,0,-1,1]
def bfs(y, x):
    res=0
    q = deque()
    q.append([y,x])
    discovered[y][x]=True
    while q:
        res+=1
        y, x = q.popleft()
        for i in range(4):
            lx = x + dx[i]
            ly = y + dy[i]
            if 0<=lx<N and 0<=ly<N:
                if discovered[ly][lx]==False and house[ly][lx]==1:
                    discovered[ly][lx]=True
                    q.append([ly, lx])
    return res

cnt=0
lst=[]
for i in range(N):
    for j in range(N):
        if house[i][j]==1 and discovered[i][j]==False:
            lst.append(bfs(i,j))
            cnt+=1
print(cnt)
lst.sort()
for l in lst:
    print(l)