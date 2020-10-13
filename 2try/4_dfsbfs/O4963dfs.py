import sys
dx = [1,-1,0,0,1,1,-1,-1]
dy = [0,0,1,-1,1,-1,1,-1]

def dfs(y, x):
    stack = [[y,x]]
    while stack:
        y, x = stack.pop()
        visited[y][x]=True
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<w and 0<=ny<h:
                if mmap[ny][nx]==1 and visited[ny][nx]==False:
                    stack.append([ny,nx])

while True:
    w, h = map(int, sys.stdin.readline().split())
    if w==0 and h==0:
        break
    mmap = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
    visited = [[False]*w for _ in range(h)]
    count = 0
    for y in range(h):
        for x in range(w):
            if mmap[y][x]==1 and visited[y][x]==False:
                dfs(y, x)
                count += 1
    print(count)

