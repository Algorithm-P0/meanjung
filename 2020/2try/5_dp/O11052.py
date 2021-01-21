import sys
N = int(sys.stdin.readline())
cards=[0]
cards.extend(list(map(int, sys.stdin.readline().split())))
dp=[0]*(N+1)
dp[1]=cards[1]
for i in range(2, N+1):
    dp[i]=cards[i]
    for j in range(i-1,i//2-1,-1):
        dp[i]=max(dp[i], dp[j]+dp[i-j])
print(dp[N])