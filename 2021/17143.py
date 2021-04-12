# r세로 c가로 s속력 d이동방향 z크기
# d 1위 2아래 3오른쪽 4왼쪽
import sys
R, C, M = map(int, sys.stdin.readline().split())
dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]
graph = [[0]*C for _ in range(R)]
for i in range(1, M+1):
    y, x, s, d, z = map(int, sys.stdin.readline().split())
    graph[y-1][x-1]=[s, d-1, z]

def fish_move():
    temp = [[0]*C for _ in range(R)]
    for y in range(R):
        for x in range(C):
            if graph[y][x]!=0:
                ly, lx, s, d, z = y, x, graph[y][x][0], graph[y][x][1], graph[y][x][2]
                while s>0:
                    ly += dy[d]
                    lx += dx[d]
                    if 0<=ly<R and 0<=lx<C:
                        s-=1
                    else:
                        ly -= dy[d]
                        lx -= dx[d]
                        if d==0:
                            d=1
                        elif d==1:
                            d=0
                        elif d==2:
                            d=3
                        elif d==3:
                            d=2
                if temp[ly][lx]==0:
                    temp[ly][lx] = [graph[y][x][0], d, z]
                else:
                    if temp[ly][lx][2]<z:
                        temp[ly][lx]=[graph[y][x][0], d, z]
    return temp

get = 0
for x in range(C):
    for y in range(R):
        if graph[y][x]!=0:
            get+=graph[y][x][2]
            graph[y][x]=0
            break
    graph = fish_move()
print(get)