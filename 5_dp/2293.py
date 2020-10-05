# 직관적으로는 알겠지만 자세히는 잘 모르겠는..?
import sys
n, k = map(int, sys.stdin.readline().split())
coins = []
for i in range(n):
    coins.append(int(sys.stdin.readline()))
dp=[0]*(k+1)
dp[0]=1
for i in coins:
    for j in range(i, k+1):
        dp[j]+=dp[j-i]
print(dp[k])
