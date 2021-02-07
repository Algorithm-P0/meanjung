import sys
N, M, K = map(int, sys.stdin.readline().split())
# aN개 zM개
dp = [[1]*(M+1) for _ in range(N+1)]
dp[1][1]=2
for y in range(N+1):
    for x in range(M+1):
        if y==0 or x==0:
            continue
        dp[y][x] = dp[y-1][x]*(y+x)//y
ans = ''
def findFunc(N, M, K):
    global ans
    if N==0:
        for i in range(M):
            ans += 'z'
        return
    if M==0:
        for i in range(N):
            ans += 'a'
        return
    if dp[N-1][M]>=K:
        ans += 'a'
        findFunc(N-1, M, K)
    else:
        ans += 'z'
        findFunc(N, M-1, K-dp[N-1][M])
    return

if dp[N][M]<K:
    print(-1)
else:
    findFunc(N, M, K)
    print(ans)