import sys
N = int(sys.stdin.readline())
"""
# 이 방법 말고 다른 방법으로 풀기(dp)
dp=[0]*91
dp[1]=1
dp[2]=1
for i in range(3, N+1):
    dp[i]=dp[i-1]+dp[i-2]
print(dp[N])
"""
