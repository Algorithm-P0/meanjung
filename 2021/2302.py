import sys
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
fixed = []
for _ in range(M):
    fixed.append(int(sys.stdin.readline()))
dp = [0]*41
dp[0]=1
dp[1]=1
for i in range(2, 41):
    dp[i]=dp[i-1]+dp[i-2]
pre = 0
ans=1
if M>0:
    for i in range(M):
        e = fixed[i]
        ans *= dp[e-pre-1]
        pre = e
    ans *= dp[N-e]
else:
    ans = dp[N]
print(ans)
