import sys
n = int(sys.stdin.readline())
wine = [0]
for _ in range(n):
    wine.append(int(sys.stdin.readline()))
dp=[0]*(n+1)
# dp[i] : i번째까지의 포도주가 있을 때 최대로 마신 양
dp[1]=wine[1]
if n>=2:
    dp[2]=wine[2]+wine[1]
    for i in range(3, n+1):
        dp[i]=max(dp[i-1], dp[i-2]+wine[i], dp[i-3]+wine[i-1]+wine[i])
print(dp[-1])