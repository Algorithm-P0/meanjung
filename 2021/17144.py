import sys
from copy import deepcopy
R, C, T = map(int, sys.stdin.readline().split())
A = []
clearIdx = []
dy = [1,-1,0,0]
dx = [0,0,-1,1]
for i in range(R):
    row = list(map(int, sys.stdin.readline().split()))
    A.append(row)
    for j in range(C):
        if A[i][j]==-1:
            clearIdx.append([i, j])
ty, tx = clearIdx[0][0], clearIdx[0][1]
by, bx = clearIdx[1][0], clearIdx[1][1]

def spread():
    temp = [[0]*C for _ in range(R)]
    temp[ty][tx]=-1
    temp[by][bx]=-1
    for y in range(R):
        for x in range(C):
            if A[y][x]>0:
                cnt = 0
                for i in range(4):
                    ny = y + dy[i]
                    nx = x + dx[i]
                    if 0<=ny<R and 0<=nx<C and A[ny][nx]!=-1:
                        cnt+=1
                        temp[ny][nx]+=A[y][x]//5
                temp[y][x]+=A[y][x]-(A[y][x]//5*cnt)
    return temp

def clear(y, x, dir):
    temp = deepcopy(A)
    cy, cx = y, x-1
    A[y][x]=0
    for i in range(4):
        while True:
            ny = y + dy[dir[i]]
            nx = x + dx[dir[i]]
            if nx==cx and ny==cy:
                return
            if 0<=nx<C and 0<=ny<R:
                A[ny][nx]=temp[y][x]
            else:
                break
            y, x = ny, nx
for t in range(T):
    A = spread()
    clear(ty, tx+1, [3,1,2,0])
    clear(by, bx+1, [3,0,2,1])
A[ty][tx]=0
A[by][bx]=0
res = 0
for a in A:
    res+=sum(a)
print(res)