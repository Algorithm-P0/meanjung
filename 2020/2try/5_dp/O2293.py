import sys
N, K = map(int, sys.stdin.readline().split())
coins = []
for _ in range(N):
    coins.append(int(sys.stdin.readline()))
dp=[0]*(K+1)
for i in coins:
    for j in range(i, K+1):
        dp[i]+=dp[j-i]
print(dp[K])