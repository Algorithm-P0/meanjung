import sys
T = int(sys.stdin.readline())
for _ in range(T):
    K = int(sys.stdin.readline())
    data = list(map(int, sys.stdin.readline().split()))
    dp=[[0]*K for _ in range(K)]
    # dp[i][j] : i에서 j까지 합치는데 드는 최소 비용
    # 초기화
    for y in range(K-1):
        dp[y][y+1]=data[y]+data[y+1]
        for x in range(y+2, K):
            dp[y][x]=dp[y][x-1]+data[x]
    
    for d in range(2, K):
        for y in range(K-d):
            x = y + d
            minimun = [dp[y][k]+dp[k+1][x] for k in range(y,x)]
            dp[y][x]+=min(minimun)
    print(dp[0][-1])
