import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
dp = [ x for x in A]
for i in range(1, N):
    dp[i]=max(dp[i], dp[i-1]+A[i])
print(max(dp))