import sys
from collections import deque
dy = [-1,1,0,0]
dx = [0,0,-1,1]
puyo = [list(sys.stdin.readline().strip()) for _ in range(12)]

def bfs(y, x, color):
    q = deque()
    q.append([y, x])
    temp = [[y,x]]#visited의 역할
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<12 and 0<=nx<6:
                if puyo[ny][nx]==color and [ny, nx] not in temp:
                    temp.append([ny,nx])
                    q.append([ny,nx])
    return temp
cnt = 0

def down():
    for y in range(10, -1, -1):
        for x in range(6):
            if puyo[y][x]!='.' and puyo[y+1][x]=='.':
                for k in range(y+1, 12):
                    if k==11 and puyo[k][x]=='.':
                        puyo[k][x]=puyo[y][x]
                    elif puyo[k][x]!='.':
                        puyo[k-1][x] = puyo[y][x]
                        break
                puyo[y][x]='.'

while True:
    visited = [[False]*6 for _ in range(12)]
    flag = 0
    for y in range(11, -1, -1):
        for x in range(6):
            if visited[y][x]==False and puyo[y][x]!='.':
                visited[y][x]=True
                temp = bfs(y, x, puyo[y][x])
                if len(temp)>=4:
                    flag = 1
                    for y, x in temp:
                        puyo[y][x]='.'
    if flag==0:
        break
    cnt+=1
    down()
print(cnt)

