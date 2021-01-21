import sys
from collections import deque
R, C = map(int, sys.stdin.readline().split())
mmap = [list(map(str, sys.stdin.readline().strip())) for _ in range(R)]
dx = [1,-1,0,0]
dy = [0,0,-1,1]
distance = [[0]*C for _ in range(R)]
water_q=deque()
hedgehog_q=deque()
for y in range(R):
    for x in range(C):
        if mmap[y][x]=='D':
            biber_y = y
            biber_x = x
            continue
        if mmap[y][x]=='S':
            hedgehog_q.append([y,x])
            continue
        if mmap[y][x]=='*':
            water_q.append([y,x])
            continue
flag = 0
while hedgehog_q:
    water_extend=[]
    hedgehog_extend=[]
    while water_q:
        y, x = water_q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<R and 0<=nx<C:
                if distance[ny][nx]==0 and mmap[ny][nx]!='X' and mmap[ny][nx]!='D' and mmap[ny][nx]!='*':
                    mmap[ny][nx]='*'
                    water_extend.append([ny,nx])
    while hedgehog_q:
        y, x = hedgehog_q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<R and 0<=nx<C:
                if distance[ny][nx]==0 and mmap[ny][nx]=='.':
                    hedgehog_extend.append([ny,nx])
                    distance[ny][nx]=distance[y][x]+1
                    continue
                if mmap[ny][nx]=='D':
                    distance[ny][nx]=distance[y][x]+1
                    flag = 1
                    break
        if flag==1:
            break
    if flag==1:
        break
    water_q.extend(water_extend)
    hedgehog_q.extend(hedgehog_extend)
if distance[biber_y][biber_x]==0:
    print("KAKTUS")
else:
    print(distance[biber_y][biber_x])