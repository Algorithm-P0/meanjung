import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())
# 가로: M, 세로: N
miro = []
counts = [[-1]*(M) for _ in range(N)]
dx = [1,-1,0,0]
dy = [0,0,-1,1]
def solve():
    q = deque()
    q.append([0,0])
    counts[0][0]=0
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0<=ny<N and 0<=nx<M:
                if counts[ny][nx]==-1 and miro[ny][nx]=='0':
                    counts[ny][nx]=counts[y][x]
                    q.appendleft([ny, nx])
                if counts[ny][nx]==-1 and miro[ny][nx]=='1':
                    counts[ny][nx]=counts[y][x]+1
                    miro[ny][nx]='0'
                    q.append([ny, nx])
    return counts[N-1][M-1]


for _ in range(N):
    miro.append(list(map(str, sys.stdin.readline().strip())))
print(solve())