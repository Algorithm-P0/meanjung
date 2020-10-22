# 수가 같거나 커지면 오르막수
import sys
N = int(sys.stdin.readline())
dp = [[0]*10 for _ in range(N+1)]
for i in range(10):
    dp[1][i]=1
for i in range(2, N+1):
    for j in range(10):
        s = 0
        for k in range(j+1):
            s += dp[i-1][k]
        dp[i][j]=s%10007
print(sum(dp[N])%10007)
