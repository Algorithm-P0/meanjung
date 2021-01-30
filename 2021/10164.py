import sys
N, M, K = map(int, sys.stdin.readline().split())
"""
def factorial(x):
    res = 1
    for i in range(x, 0, -1):
        res*=i
    return res
if K==0:
    print(factorial(M+N-2)//(factorial(M-1)*factorial(N-1)))
else:
    y = K//M
    x = K%M-1
    f1 = factorial(x+y)//(factorial(x)*factorial(y))
    f2 = factorial(M+N-2-x-y)//(factorial(M-1-x)*factorial(N-1-y))
    print(f1*f2)
"""
dp = [[0]*(M+1) for _ in range(N+1)]
dp[0][1]=1
cnt=1
for y in range(1, N+1):
    for x in range(1, M+1):
        if cnt==K:
            py = y
            px = x
        cnt+=1
        dp[y][x] = dp[y-1][x]+dp[y][x-1]
if K==0:
    print(dp[N][M])
else:
    print(dp[py][px]*dp[N-py+1][M-px+1])