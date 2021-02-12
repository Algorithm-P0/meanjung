import sys
k=1
dp=[[0]*3 for _ in range(100001)]
while True:
    N = int(sys.stdin.readline())
    if N == 0:
        break
    for i in range(N):
        dp[i]=list(map(int, sys.stdin.readline().split()))
    dp[1][0]=dp[1][0]+dp[0][1]
    dp[1][1]=min(dp[1][1]+dp[1][0], min(dp[0][1]+dp[0][2]+dp[1][1], dp[1][1]+dp[0][1]))
    dp[1][2]=min(dp[1][1]+dp[1][2], min(dp[1][2]+dp[0][1],dp[1][2]+dp[0][1]+dp[0][2]))
    for i in range(2, N):
        dp[i][0]+=min(dp[i-1][1], dp[i-1][0])
        dp[i][1]+=min(dp[i-1][0], dp[i-1][1], dp[i-1][2], dp[i][0])
        dp[i][2]+=min(dp[i][1], dp[i-1][2], dp[i-1][1])
    print(str(k)+'.',dp[N-1][1])
    k+=1