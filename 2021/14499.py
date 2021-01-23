import sys
N, M, y, x, K = map(int, sys.stdin.readline().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))
order = list(map(int, sys.stdin.readline().split()))
dice = [0,0,0,0,0,0,0]
#d 1동 2서 3북 4남
dy = [0,0,0,-1,1]
dx = [0,1,-1,0,0]

def move(direction):
    if direction == 1:
        dice[1], dice[3], dice[4], dice[6] = dice[3], dice[6], dice[1], dice[4]
    elif direction == 2:
        dice[1], dice[3], dice[4], dice[6] = dice[4], dice[1], dice[6], dice[3]
    elif direction == 3:
        dice[1], dice[2], dice[5], dice[6] = dice[2], dice[6], dice[1], dice[5]
    elif direction == 4:
        dice[1], dice[2], dice[5], dice[6] = dice[5], dice[1], dice[6], dice[2]

for i in order:
    if 0<=y+dy[i]<N and 0<=x+dx[i]<M:
        y+=dy[i]
        x+=dx[i]
        move(i)
        if graph[y][x]!=0:
            dice[1]=graph[y][x]
            graph[y][x]=0
        else:
            graph[y][x]=dice[1]
        print(dice[6])