import sys
N = int(sys.stdin.readline())
dp = [[0]*3 for _ in range(N+1)]
for i in range(3):
    dp[1][i] = 1
for i in range(2, N+1):
    # 맨 윗줄에 사자가 왼쪽에 있을 경우
    dp[i][0] = (dp[i-1][1]+dp[i-1][2])%9901
    # 맨 윗줄에 사자가 오른쪽에 있을 경우
    dp[i][1] = (dp[i-1][0]+dp[i-1][2])%9901
    # 맨 윗줄에 사자가 하나도 없을 경우
    dp[i][2] = (dp[i-1][0]+dp[i-1][1]+dp[i-1][2])%9901
print(sum(dp[N])%9901)