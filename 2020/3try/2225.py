import sys
N, K = map(int, sys.stdin.readline().split())
dp = [[0]*(N+1) for _ in range(K+1)]
for i in range(1, K+1):
    for j in range(N+1):
        if i==1:
            dp[i][j]=1
        else:
            if j==0:
                dp[i][j]=1
            else:
                dp[i][j]=(dp[i-1][j]+dp[i][j-1])%1000000000
print(dp[-1][-1]%1000000000)