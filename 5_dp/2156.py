import sys
n = int(sys.stdin.readline())
drink=[0]
for _ in range(n):
    drink.append(int(sys.stdin.readline()))
dp=[0]*(n+1)
dp[1]=drink[1]
if n>=2:
    dp[2]=drink[2]+drink[1]
    for i in range(3,n+1):
        dp[i]=max(dp[i-1],dp[i-2]+drink[i], dp[i-3]+drink[i-1]+drink[i])
print(dp[-1])