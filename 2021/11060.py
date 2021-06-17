import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

dp = [-1]*N

def bfs():
    q = [0]
    dp[0]=0
    while q:
        now = q.pop(0)
        jump = A[now]
        for i in range(jump, 0, -1):
            if now+i<N and dp[now+i]==-1:
                dp[now+i] = dp[now]+1
                q.append(now+i)
bfs()
print(dp[-1])
