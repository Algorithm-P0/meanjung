import sys
N = int(sys.stdin.readline())
dp = [0]*(N+1)
square = [i*i for i in range(1, N+1)]
for i in range(1, N+1):
    s=[]
    for j in square:
        if j>i:
            break
        s.append(dp[i-j])
    dp[i]=min(s)+1
print(dp[N])
