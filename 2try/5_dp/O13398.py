import sys
n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
dp= [[0,0] for _ in range(n)]
dp[0]=[lst[0], -sys.maxsize]
for i in range(1, n):
    dp[i][0]=max(dp[i-1][0]+lst[i], lst[i])
    dp[i][1]=max(dp[i-1][0], dp[i-1][1]+lst[i])
res=-sys.maxsize
for i in range(n):
    a = max(dp[i])
    res = max(res, a)
print(res)