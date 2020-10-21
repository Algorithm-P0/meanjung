import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
dp=[0]*N
dp[0]=1
# dp[i] : i번째 값을 포함하는 LIS의 길이
for i in range(1, N):
    m = 0
    for j in range(i-1,-1,-1):
        if A[i]>A[j] and m<dp[j]:
            m = dp[j]
    if m==0:
        dp[i]=1
    else:
        dp[i]=m+1
print(max(dp))
