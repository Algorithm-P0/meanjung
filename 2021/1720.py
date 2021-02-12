import sys
N = int(sys.stdin.readline())
dp = [0]*31
dp[1]=1
for i in range(2, 31):
    dp[i]=dp[i-1]+dp[i-2]*2
if N%2==1:
    print((dp[N]+dp[(N-1)//2])//2)
else:
    print((dp[N]+dp[N//2]+dp[N//2-1]*2)//2)