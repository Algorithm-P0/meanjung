import sys
n = int(sys.stdin.readline())
dp = [0]*10001
for i in range(1, n+1):
    if i==1:
        dp[i]=1
    else:
        dp[i]=dp[i-1]+dp[i-2]
print(dp[n])