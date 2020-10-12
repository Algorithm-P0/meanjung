import sys
N = int(sys.stdin.readline())
triangle = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp=[[0]*N for _ in range(N)]
dp[0][0]=triangle[0][0]
for i in range(N-1):
    for j in range(len(triangle[i])):
        dp[i+1][j]=max(dp[i+1][j], dp[i][j]+triangle[i+1][j])
        dp[i+1][j+1]=max(dp[i+1][j+1], dp[i][j]+triangle[i+1][j+1])
print(max(dp[-1]))