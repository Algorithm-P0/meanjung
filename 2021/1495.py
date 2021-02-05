# N곡의개수 S시작볼륨 M제한볼륨
# 마지막 곡을 연주할 수 있는 볼륨 중 최댓값
import sys
N, S, M = map(int, sys.stdin.readline().split())
vol = list(map(int, sys.stdin.readline().split()))
dp = [[0]*(M+1) for _ in range(N+1)]
dp[0][S]=1
for y in range(1, N+1):
    for x in range(M+1):
        if dp[y-1][x]==0:
            continue
        if x+vol[y-1]<=M:
            dp[y][x+vol[y-1]]=1
        if x-vol[y-1]>=0:
            dp[y][x-vol[y-1]]=1
idx = -1
for x in range(M, -1, -1):
    if dp[-1][x]==1:
        idx = x
        break
print(idx)