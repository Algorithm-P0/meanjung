import sys
N, M = map(int, sys.stdin.readline().split())
candy = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[0]*M for _ in range(N)]
dp[0][0]=candy[0][0]
dy = [1, 0, 1]
dx = [0, 1, 1]
for y in range(N):
    for x in range(M):
        for i in range(3):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<N and 0<=nx<M:
                dp[ny][nx]=max(dp[ny][nx], dp[y][x]+candy[ny][nx])
print(dp[-1][-1])