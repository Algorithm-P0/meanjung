import sys
N=int(sys.stdin.readline())
A=[0]
A.extend(list(map(int, sys.stdin.readline().split())))
dp=[0]*(N+1)
dp[1]=A[1]
for i in range(2, N+1):
    dp[i]=A[i]
    for j in range(1,i):
        if A[i]>A[j]:
            dp[i]=max(dp[i],dp[j]+A[i])
print(max(dp))