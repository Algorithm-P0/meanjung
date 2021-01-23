import sys
N, M = map(int, sys.stdin.readline().split())
# 세로 N, 가로 M
y, x, d = map(int, sys.stdin.readline().split())
# 청소기 좌표, 바라보는 방향
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))
# d 0북 1동 2남 3서
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
cnt=1

while True:
    flag = 0
    graph[y][x]=2
    for _ in range(4):
        d = (d+3)%4
        if graph[y+dy[d]][x+dx[d]]==0:
            y+=dy[d]
            x+=dx[d]
            flag=1
            cnt+=1
            break
    if flag==0:
        if graph[y-dy[d]][x-dx[d]]==1:
            break
        y-=dy[d]
        x-=dx[d]
print(cnt)