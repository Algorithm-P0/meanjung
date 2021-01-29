"""
import sys
N = int(sys.stdin.readline())
children = list(map(int, sys.stdin.readline().split()))
dp = [0]*(N+1)
long = 0
for i in range(N):
    idx = children[i]
    dp[idx]=dp[idx-1]+1
    long = max(dp[idx], dp[idx-1]+1)
print(N-long)
# 최장 연속되는 증가수열로 풀었는데
# 다른 모범답안 참고해서 풀었는데
# 왜 틀렸는지 모르겠음
"""
import sys
N = int(sys.stdin.readline())
children = [0]
children.extend(list(map(int, sys.stdin.readline().split())))
position = [0]*(N+1)
for i in range(1, N+1):
    position[children[i]]=i
count = 1
mmax = -1
for i in range(1, N):
    if position[i]<position[i+1]:
        count+=1
        mmax = max(mmax, count)
    else:
        count=1
print(N-mmax)