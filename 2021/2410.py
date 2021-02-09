import sys
N = int(sys.stdin.readline())
nums = [2**x for x in range(21)]
dp = [0]*(N+1)
dp[0]=1
for num in nums:
    if num<=N:
        for j in range(num, N+1):
            dp[j]=(dp[j]+dp[j-num])%1000000000
print(dp[-1]%1000000000)
