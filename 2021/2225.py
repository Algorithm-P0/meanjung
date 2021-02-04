import sys
N, K = map(int, sys.stdin.readline().split())
dp = [[0]*(N+1) for _ in range(K+1)]
for y in range(1, K+1):
    for x in range(N+1):
        if y == 1 or x==0:
            dp[y][x]=1
            continue
        dp[y][x] = (dp[y-1][x]+dp[y][x-1])%1000000000
print(dp[K][N]%1000000000)
"""
규칙을 찾아서 풀긴했지만
왜 그런 규칙이 생기는 지는 모르겠다...
"""