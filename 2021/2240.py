import sys
T, W = map(int, sys.stdin.readline().split())
# T초 동안 자두가 떨어진다.
# 최대 W번 움직인다.
tree = []
for _ in range(T):
    tree.append(int(sys.stdin.readline()))
dp = [[[0]*32 for _ in range(1001)] for _ in range(3)]
# dp[자두나무위치][떨어지는시간][최대움직일수있는횟수]
for i in range(1, T+1):
    for j in range(1, W+2):
        if tree[i-1]==1:
            dp[1][i][j]=max(dp[1][i-1][j]+1, dp[2][i-1][j-1]+1)
            dp[2][i][j]=max(dp[1][i-1][j-1], dp[2][i-1][j])
        else:
            if i==1 and j==1:
                continue
            dp[1][i][j]=max(dp[1][i-1][j-1], dp[2][i-1][j])
            dp[2][i][j]=max(dp[1][i-1][j-1]+1, dp[2][i-1][j]+1)
print(max(max(dp[1][T]), max(dp[2][T])))

# 풀이 참조
# https://mygumi.tistory.com/140
# 왜 W+1까지 반복문을 도는가
# else에서 왜 1&1일때 continue인가