dp=[[0]*31 for _ in range(31)]
for i in range(1,31):
    dp[i][1]=1
    dp[i][i]=1
for i in range(3,31):
    for j in range(2,i):
        dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
import sys
n,k=map(int,sys.stdin.readline().split())
print(dp[n][k])