import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
dp=[0]*N
dp[0]=1
for i in range(1, N):
    m = 0
    for j in range(i-1,-1,-1):
        if A[i]<A[j] and m<dp[j]:
            m = dp[j]
    dp[i] = m + 1
print(max(dp))