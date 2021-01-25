import sys
# 0 1 2 3
dx = [1,0,-1,0]
dy = [0,-1,0,1]
N = int(sys.stdin.readline())
location = [[0]*101 for _ in range(101)]

for _ in range(N):
    x, y, d, g = map(int, sys.stdin.readline().split())
    location[y][x]=1
    move = [d]
    for _ in range(g):
        temp = []
        for i in range(len(move)):
            temp.append((move[-i-1]+1)%4)
        move.extend(temp)
    for i in move:
        nx = x + dx[i]
        ny = y + dy[i]
        location[ny][nx]=1
        y, x = ny, nx

result = 0
for y in range(100):
    for x in range(100):
        if location[y][x] and location[y][x+1] and location[y+1][x] and location[y+1][x+1]:
            result+=1
print(result)

