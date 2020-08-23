import sys
N = int(sys.stdin.readline())
T=[]
P=[]
for _ in range(N):
    t, p = map(int, sys.stdin.readline().split())
    T.append(t)
    P.append(p)
"""
dp[i] : i일부터 얻을 수 있는 최대 이익
"""
dp=[0]*(N+1)
for i in range(N-1,-1,-1):
    if i+T[i]>N:
        dp[i]=dp[i+1]
    else:
        dp[i]=max(dp[i+1], dp[i+T[i]]+P[i])
print(dp[0])
