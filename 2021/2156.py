# dp[i]를 i번째 포도주를 꼭 마신 상태로 할 것이냐
# 아님 i번째 포도주까지 존재하는 것으로 판단할 것이냐
import sys
n = int(sys.stdin.readline())
wine = [0]
for _ in range(n):
    wine.append(int(sys.stdin.readline()))
dp=[0]*(n+1)
dp[1]=wine[1]
if n>=2:
    dp[2]=wine[1]+wine[2]
    for i in range(3, n+1):
        dp[i]=max(dp[i-1], dp[i-2]+wine[i], dp[i-3]+wine[i-1]+wine[i])
print(dp[-1])