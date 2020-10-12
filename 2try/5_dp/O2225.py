import sys
N, K = map(int, sys.stdin.readline().split())
dp=[[0]*201 for _ in range(201)]
# dp[i][j] : i개로 j값을 만드는 개수
for i in range(N+1):
    dp[0][i]=0
    dp[1][i]=1
for i in range(2, K+1):
    for j in range(N+1):
        for l in range(j+1):
            dp[i][j]=(dp[i][j]+dp[i-1][j-l])%1000000000
print(dp[K][N])