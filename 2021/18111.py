import sys
N, M, B = map(int, sys.stdin.readline().split())
# 세로N 가로M 인벤토리B
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
leastTime = sys.maxsize
for h in range(257):
    build = 0
    remove = 0
    for y in range(N):
        for x in range(M):
            height = graph[y][x]-h
            if height>0:
                remove += height
            elif height<0:
                build -= height
    if remove+B>=build:
        time = 2*remove+build
        if time<=leastTime:
            leastTime = time
            mostHeight = h
print(leastTime, mostHeight)