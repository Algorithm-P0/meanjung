dp=[[0]*30 for _ in range(30)]
# 초기화
for i in range(30):
    dp[1][i]=i
for i in range(2, 30):
    for j in range(i, 30): # i<=j
        for k in range(i-1,j):
            dp[i][j]+=dp[i-1][k]
import sys
T=int(sys.stdin.readline())
for _ in range(T):
    N, M =map(int, sys.stdin.readline().split())
    print(dp[N][M])