# 알듯말듯 까다롭다.
import sys
N = int(sys.stdin.readline())
A=list(map(int, sys.stdin.readline().split()))
dp=[[0,0] for _ in range(N)]
dp[0]=[A[0], -float('inf')]
for i in range(1, N):
    dp[i][0]=max(dp[i-1][0]+A[i], A[i])
    """
    dp[i][0] : 그냥 연속합
    아무것도 제거하지 않고
    A[i]를 꼭 포함하는 최대 연속합
    """
    dp[i][1]=max(dp[i-1][0], dp[i-1][1]+A[i])
    """
    dp[i][1] : 하나가 제거된 최대 연속합
    """
res=-float('inf')
for a in range(N):
    res = max(res, max(dp[a]))
print(res)