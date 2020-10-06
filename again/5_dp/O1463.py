"""
# 맞는 풀이
# 시간이 상대적으로 많이 걸렸다.
import sys
from collections import deque
N = int(sys.stdin.readline())
dp = [0]*(N+1)
visited=[False]*(N+1)
stack = deque()
stack.append(N)
while stack:
    p = stack.popleft()
    visited[p]=True
    if p-1>=1:
        if visited[p-1]==True:
            dp[p-1]=min(dp[p-1],dp[p]+1)
        else:
            dp[p-1]=dp[p]+1
            visited[p-1]=True
            stack.append(p-1)
    if p%2==0:
        if visited[p//2]==True:
            dp[p//2]=min(dp[p//2],dp[p]+1)
        else:
            dp[p//2]=dp[p]+1
            visited[p//2]=True
            stack.append(p//2)
        
    if p%3==0:
        if visited[p//3]==True:
            dp[p//3]=min(dp[p//3], dp[p]+1)
        else:
            dp[p//3]=dp[p]+1
            visited[p//3]=True
            stack.append(p//3)
print(dp[1])
"""
import sys
N = int(sys.stdin.readline())
dp=[0]*(N+1)
for i in range(2, N+1):
    dp[i]=dp[i-1]+1
    if i%2==0:
        dp[i]=min(dp[i], dp[i//2]+1)
    if i%3==0:
        dp[i]=min(dp[i], dp[i//3]+1)
print(dp[N])