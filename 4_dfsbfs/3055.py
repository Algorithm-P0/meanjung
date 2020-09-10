import sys
from collections import deque
R, C = map(int, sys.stdin.readline().split())
# R : 세로 / C : 가로
forest = [list(map(str, sys.stdin.readline().strip())) for _ in range(R)]
# S : 고슴도치 / * : 물 / X : 돌 / D : 비버 굴
water = deque()
hedgehog = deque()
dx=[0,0,-1,1]
dy=[1,-1,0,0]
for i in range(R):
    for j in range(C):
        if forest[i][j]=='S':
            hedgehog.append([i,j,0])
            forest[i][j]=0
            continue
        if forest[i][j]=='*':
            water.append([i,j])
            continue
        if forest[i][j]=='D':
            Y = i
            X = j
flag=0
res='KAKTUS'
while water or hedgehog:
    water_extend=[]
    hedgehog_extend=[]
    while water:
        y, x = water.popleft()
        for i in range(4):
            ly = y + dy[i]
            lx = x + dx[i]
            if 0<=lx<C and 0<=ly<R:
                if forest[ly][lx]!='*' and forest[ly][lx]!='X' and forest[ly][lx]!='D':
                    forest[ly][lx]='*'
                    water_extend.append([ly,lx])
    while hedgehog:
        y, x, value = hedgehog.popleft()
        for i in range(4):
            ly = y + dy[i]
            lx = x + dx[i]
            if 0<=lx<C and 0<=ly<R:
                if forest[ly][lx]=='.':
                    forest[ly][lx]=value+1
                    hedgehog_extend.append([ly,lx,forest[ly][lx]])
                if ly==Y and lx==X:
                        res=value+1
                        flag=1
                        break
        if flag==1:
            break
    if flag==1:
        break
    water.extend(water_extend)
    hedgehog.extend(hedgehog_extend)
print(res)