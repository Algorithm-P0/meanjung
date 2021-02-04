import sys
T = int(sys.stdin.readline())
k = int(sys.stdin.readline())
coin = [[0,0]]
for _ in range(k):
    coin.append(list(map(int, sys.stdin.readline().split())))
coin.sort()
dp =[[0]*(T+1) for _ in range(k+1)]
for y in range(k+1):
    dp[y][0]=1
for y in range(1, k+1):
    for num in range(coin[y][1]+1):
        # num번 사용했을때
        for x in range(T+1):
            temp = x + num*coin[y][0]
            if temp == 0:
                continue
            if temp<T+1:
                dp[y][temp] += dp[y-1][x]
            else:
                break
print(dp[k][T])