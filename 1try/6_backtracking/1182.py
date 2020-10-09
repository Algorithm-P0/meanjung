# 브루트포스, 백트래킹은 자주 같이 분류되는 듯.
import sys
N, S = map(int, sys.stdin.readline().split())
nList = list(map(int, sys.stdin.readline().split()))
ans=0
def solve(idx, sum):
    global ans
    if sum == S:
        ans+=1
    for j in range(idx+1, N):
        sum+=nList[j]
        solve(j, sum)
        sum-=nList[j]


for i in range(N):
    solve(i, nList[i])

print(ans)