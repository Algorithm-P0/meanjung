import sys
n = int(sys.stdin.readline())
dp=[[0,0] for _ in range(100001)]
dp[1]=[1,1]
dp[2]=[1,1]
for i in range(3, n+1):
    if i%2==0: # 짝수이면
        dp[i]=[dp[i-1][0]%16769023, dp[i-1][1]%16769023]
    else: # 홀수이면
        dp[i]=[sum(dp[i-1])%16769023, sum(dp[i-1])%16769023]
print(sum(dp[n])%16769023)