import sys
N = int(sys.stdin.readline())
"""
# 시간초과 풀이
import math
dp=[100001]*(N+1)
dp[0]=1
dp[1]=1
for i in range(2,N+1):
    x=math.pow(i,0.5)
    if int(x)-x!=0:
        for j in range(i-1,0,-1):
            k = math.pow(j,0.5)
            if int(k)-k==0:
                dp[i]=min(dp[i], dp[j]+dp[i-j])
    else:
        dp[i]=1
print(dp[N])
"""
dp = [0]*(N+1)
square=[i*i for i in range(1, N+1)]
for i in range(1, N+1):
    s=[]
    for j in square:
        if j>i:
            break
        s.append(dp[i-j])
    dp[i]=min(s)+1
print(dp[N])
