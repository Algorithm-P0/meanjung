import sys
N = int(sys.stdin.readline())
dp=[0]*81
dp[1]=1
dp[2]=1
for i in range(3, N+1):
    dp[i]=dp[i-1]+dp[i-2]
print(4*dp[N]+2*dp[N-1])