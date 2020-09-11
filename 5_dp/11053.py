import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
dp=[1]*N
# dp[i] : i번째 수를 마지막으로 갖는 lis 길이
# lis : Longest Increasing Subsequence
if N>1:
    for i in range(1,N):
        for j in range(i):
            if A[i]>A[j]:
                dp[i]=max(dp[i], dp[j]+1)
            """
            위 if문과 같은 내용
            if A[i]>A[j] and dp[i]<dp[j]+1:
                dp[i]=dp[j]+1
            """
print(dp)
print(max(dp))
"""
시간복잡도 : N^2
"""