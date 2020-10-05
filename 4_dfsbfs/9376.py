# 꼭 다시 풀어보기
# 이해 안감

import sys
from collections import deque
def bfs(x,y):
    dist = [[-1]*(w+2) for _ in range(h+2)]# 열어야하는 문의 개수
    q = deque()
    q.append((x,y))
    dist[x][y]=0
    while q:
        x, y = q.popleft()
        for dx, dy in (-1,0),(1,0),(0,-1),(0,1):
            nx, ny = x + dx, y + dy
            if nx<0 or nx>h+1 or ny<0 or ny>w+1:# out of range
                continue
            if dist[nx][ny]>=0 or jail[nx][ny]=='*':#벽이거나 한 번 이상 방문한 기록이 있음
                continue
            if jail[nx][ny]=='#':#문
                dist[nx][ny]=dist[x][y]+1
                q.append((nx,ny))
            elif jail[nx][ny]=='.':#그냥 빈공간
                dist[nx][ny]=dist[x][y]
                q.appendleft((nx,ny))#열어야 하는 문의 최솟값을 구해야 하므로 appendleft❗
    return dist
T = int(sys.stdin.readline())
for _ in range(T):
    h, w = map(int, sys.stdin.readline().split())
    jail=[['.']*(w+2)]
    for _ in range(h):
        jail.append(list('.'+sys.stdin.readline().strip()+'.'))
    jail.append(['.']*(w+2))
    d = deque()
    for i in range(h+2):
        for j in range(w+2):
            if jail[i][j]=='$':
                jail[i][j]='.'
                d.append((i,j))
    sx, sy = d.popleft()
    d1 = bfs(sx,sy)
    sx, sy = d.popleft()
    d2 = bfs(sx, sy)
    d3 = bfs(0,0)
    ans = 1000000000
    for i in range(h+2):
        for j in range(w+2):
            if jail[i][j]=='*':
                continue
            k = d1[i][j]+d2[i][j]+d3[i][j]
            if jail[i][j]=='#':
                k-=2
            ans = min(k, ans)
    print(ans)