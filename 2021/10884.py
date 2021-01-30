import sys
N = int(sys.stdin.readline())
dp = [[0]*10 for _ in range(N+1)]
dp[1] = [0,1,1,1,1,1,1,1,1,1]
for i in range(2, N+1):
    dp[i][1]=dp[i-1][0]
    dp[i][8]=dp[i-1][9]
    for j in range(1, 9):
        dp[i][j-1]=(dp[i][j-1]+dp[i-1][j]%1000000000)
        dp[i][j+1]=(dp[i][j+1]+dp[i-1][j]%1000000000)
print(sum(dp[N])%1000000000)