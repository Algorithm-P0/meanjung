import sys
from collections import deque
dy = [1,-1,0,0]
dx = [0,0,-1,1]
puyo = []
for _ in range(12):
    puyo.append(list(map(str, sys.stdin.readline().strip())))

def bfs(y, x, flag):
    visited = [[0]*6 for _ in range(12)]
    cnt=1
    visited[y][x]=cnt
    q = deque()
    q.append([y, x])
    count = 0
    while q:
        y, x = q.popleft()
        count+=1
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0<=ny<12 and 0<=nx<6:
                if puyo[y][x]==puyo[ny][nx] and visited[ny][nx]==0:
                    visited[ny][nx]=1
                    cnt+=1
                    q.append([ny, nx])
    if count>=4:
        flag+=1
        for i in range(12):
            for j in range(6):
                if visited[i][j]==1:
                    puyo[i][j]='.'
    return flag

def fall():
    for y in range(10, -1, -1):
        for x in range(6):
            if puyo[y][x]!='.' and puyo[y+1][x]=='.':
                for k in range(y+1, 12):
                    if k==11 and puyo[k][x]=='.':
                        puyo[k][x] = puyo[y][x]
                    elif puyo[k][x]!='.':
                        puyo[k-1][x]=puyo[y][x]
                puyo[y][x]='.'
ans=0
while True:
    cnt=0
    visited = [[0]*6 for _ in range(12)]
    for y in range(12):
        for x in range(6):
            if puyo[y][x]!='.':
                cnt = bfs(y, x, cnt)
    if cnt==0:
        print(ans)
        break
    else:
        ans+=1
    fall()