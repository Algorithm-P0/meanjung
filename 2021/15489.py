import sys
R, C, W = map(int, sys.stdin.readline().split())
dp = [[0]*31 for _ in range(31)]
dp[1][1]=1
for y in range(1, 31):
    for x in range(1, y+1):
        if x==1 or y==x:
            dp[y][x]=1
        else:
            dp[y][x]=dp[y-1][x-1]+dp[y-1][x]
sum = 0
for y in range(1, W+1):
    for x in range(y):
        sum += dp[R+y-1][C+x]
print(sum)