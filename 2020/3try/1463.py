import sys

X = int(sys.stdin.readline())
dp = [sys.maxsize]*(X+1)
dp[X]=0
def solve(p):
    tmp = []
    while p:
        x = p.pop()
        if x==1:
            return
        if x-1>=0:
            dp[x-1]=min(dp[x-1],dp[x]+1)
            tmp.append(x-1)
        if x%2==0:
            dp[x//2]=min(dp[x//2],dp[x]+1)
            tmp.append(x//2)
        if x%3==0:
            dp[x//3]=min(dp[x//3],dp[x]+1)
            tmp.append(x//3)
    solve(tmp)
solve([X])
print(dp[1])