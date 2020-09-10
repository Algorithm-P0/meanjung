import sys
N=int(sys.stdin.readline())
dp=[[0]*2 for _ in range(N+1)]
dp[1]=[0,1]
if N>=2:
    dp[2]=[1,0]
    for i in range(3, N+1):
        dp[i][0]=dp[i-1][0]+dp[i-1][1]
        dp[i][1]=dp[i-1][0]
print(sum(dp[N]))
