import sys
N = int(sys.stdin.readline())
line = [0]*501
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    line[a]=b
dp = [0]*501
for i in range(1, 501):
    if line[i]!=0:
        dp[i]=1
        for j in range(1, i):
            if line[j]!=0 and line[i]>line[j]:
                dp[i]=max(dp[i], dp[j]+1)
print(N-max(dp))