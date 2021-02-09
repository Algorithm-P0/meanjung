import sys
T = int(sys.stdin.readline())
L = []
for _ in range(T):
    L.append(int(sys.stdin.readline()))

dp = [0]*5001
dp[0]=1
for i in range(2, 5001, 2):
    for j in range(2, i+1, 2):
        dp[i]+=(dp[j-2]*dp[i-j])%1000000007
for l in L:
    print(dp[l]%1000000007)