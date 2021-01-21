# dp

import sys

N = int(sys.stdin.readline())
T=[]
P=[]
dp=[]
for _ in range(N):
    t, p = map(int, sys.stdin.readline().split())
    T.append(t)
    P.append(p)
    dp.append(p)
dp.append(0)
"""
dp[i] : i일부터 얻을 수 있는 최대 이익
"""
for i in range(N-1, -1, -1):
    if i+T[i]>N:# 맡을 수 없는 일, 즉 i부터 시작하는 일은 할 수 없다.
        dp[i]=dp[i+1]
    else:
        dp[i]=max(dp[i+1],dp[i+T[i]]+P[i])
print(dp[0])