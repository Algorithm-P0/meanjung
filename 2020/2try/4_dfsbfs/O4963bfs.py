import sys
from collections import deque
dx = [1,-1,0,0,1,1,-1,-1]
dy = [0,0,1,-1,1,-1,1,-1]
def bfs(y, x):
    q = deque()
    q.append([y,x])
    discovered[y][x]=True
    while q:
        y, x = q.popleft()
        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<h and 0<=nx<w:
                if discovered[ny][nx]==False and mmap[ny][nx]==1:
                    q.append([ny,nx])
                    discovered[ny][nx]=True
while True:
    w, h = map(int, sys.stdin.readline().split())
    if w==0 and h==0:
        break
    mmap = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
    discovered = [[False]*w for _ in range(h)]
    count = 0
    for y in range(h):
        for x in range(w):
            if mmap[y][x]==1 and discovered[y][x]==False:
                bfs(y, x)
                count+=1
    print(count)