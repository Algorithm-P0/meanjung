import sys
N, M = map(int, sys.stdin.readline().split())
# 세로N 가로M
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
tetromino = [
    [(1,0),(0,1),(1,1)],
    [(1,0),(2,0),(3,0)],
    [(0,1),(0,2),(0,3)],
    [(1,0),(1,1),(1,2)],#ㄴ
    [(1,0),(1,-1),(1,-2)],
    [(-1,0),(-1,1),(-1,2)],
    [(-1,0),(-1,-1),(-1,-2)],
    [(1,0),(2,0),(2,-1)],
    [(1,0),(2,0),(2,1)],
    [(-1,0),(-2,0),(-2,-1)],
    [(-1,0),(-2,0),(-2,1)],
    [(0,1),(-1,1),(-1,2)],#ㄹ
    [(0,1),(1,1),(1,2)],
    [(1,0),(1,1),(2,1)],
    [(1,0),(1,-1),(2,-1)],
    [(0,-1),(-1,0),(0,1)],#ㅗ
    [(0,-1),(1,0),(0,1)],
    [(-1,0),(0,-1),(1,0)],
    [(-1,0),(0,1),(1,0)]
]

def find(y, x):
    ans = 0
    for t in tetromino:
        res = graph[y][x]
        for i in range(3):
            ny = y + t[i][0]
            nx = x + t[i][1]
            if not 0<=ny<N or not 0<=nx<M:
                break
            res+=graph[ny][nx]
        ans = max(ans, res)
    return ans

result = 0
for y in range(N):
    for x in range(M):
        result = max(result, find(y, x))
print(result)
