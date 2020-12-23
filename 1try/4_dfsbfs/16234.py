import sys
from collections import deque
N, L, R = map(int, sys.stdin.readline().split())
populate = []
for _ in range(N):
    populate.append(list(map(int, sys.stdin.readline().split())))
dy = [-1,1,0,0]
dx = [0,0,-1,1]
cnt = 0

def bfs(y, x):
    q = deque()
    q.append([y, x])
    temp = []
    temp.append([y, x])
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<N and 0<=nx<N and visit[ny][nx]==0:
                if L<=abs(populate[ny][nx]-populate[y][x])<=R:
                    visit[ny][nx]=1
                    q.append([ny, nx])
                    temp.append([ny, nx])
    return temp

while True:
    visit = [[0]*N for _ in range(N)]
    isTrue = False
    for y in range(N):
        for x in range(N):
            if visit[y][x]==0:
                visit[y][x]=1
                temp = bfs(y, x)
                if len(temp)>1:
                    isTrue = True
                    num = sum([populate[ly][lx] for ly, lx in temp])//len(temp)
                    for ly, lx in temp:
                        populate[ly][lx] = num
    if isTrue==False:
        break
    cnt+=1
print(cnt)