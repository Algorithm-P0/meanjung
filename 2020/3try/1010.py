import sys
T = int(sys.stdin.readline())
dp = [[0]*30 for _ in range(30)]
for i in range(1, 30):
    for j in range(i+1):
        if j==0 or i==j:
            dp[i][j]=1
        else:
            dp[i][j] = dp[i-1][j-1]+dp[i-1][j]
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    print(dp[M][N])