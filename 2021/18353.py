"""
가장 긴 감소하는 수열
"""
import sys
N = int(sys.stdin.readline())
soldier = list(map(int, sys.stdin.readline().split()))
dp = [1]*N
for i in range(1, N):
    for j in range(i-1,-1,-1):
        if soldier[j]>soldier[i]:
            dp[i]=max(dp[i], dp[j]+1)
print(N-max(dp))