import sys
N = int(sys.stdin.readline())
RGB = []
for _ in range(N):
    RGB.append(list(map(int, sys.stdin.readline().split())))
dp = [[0]*3 for _ in range(N)]
for i in range(3):
    dp[0][i] = RGB[0][i]
for i in range(1, N):
    dp[i][0]=RGB[i][0]+min(dp[i-1][1], dp[i-1][2])
    dp[i][1]=RGB[i][1]+min(dp[i-1][0], dp[i-1][2])
    dp[i][2]=RGB[i][2]+min(dp[i-1][0], dp[i-1][1])
print(min(dp[-1]))