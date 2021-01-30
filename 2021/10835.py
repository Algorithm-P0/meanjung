import sys
n = int(sys.stdin.readline())
left = list(map(int, sys.stdin.readline().split()))
right = list(map(int, sys.stdin.readline().split()))
dp = [[0]*(n+1) for _ in range(n+1)]
for y in range(n-1, -1, -1):
    for x in range(n-1, -1, -1):
        if right[x]<left[y]:
            dp[y][x] = max(dp[y][x+1]+right[x], dp[y][x+1], dp[y+1][x+1])
        else:
            dp[y][x] = max(dp[y+1][x], dp[y+1][x+1])
print(dp[0][0])