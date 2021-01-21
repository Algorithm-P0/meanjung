import sys
n, k = map(int, sys.stdin.readline().split())
coins = [int(sys.stdin.readline()) for _ in range(n)]
dp=[100001]*100001
# dp[i] : 가치가 i일때 동전의 사용한 최소 동전의 개수
dp[0]=0
for c in coins:
    dp[c]=1
for i in range(1, k+1):
    for j in range(n):
        if dp[i]==1:
            break
        if i-coins[j]>=0:
            dp[i]=min(dp[i], dp[i-coins[j]]+1)
if dp[k]==100001:
    print(-1)
else:
    print(dp[k])
