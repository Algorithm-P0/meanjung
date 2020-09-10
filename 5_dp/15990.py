import sys
T = int(sys.stdin.readline())
N=[]
for _ in range(T):
    N.append(int(sys.stdin.readline()))
dp=[[0]*(max(N)+1) for _ in range(3)]
dp[0][1]=1
dp[1][2]=1
dp[0][3]=1
dp[1][3]=1
dp[2][3]=1
for i in range(4,max(N)+1):
    dp[0][i]=(dp[1][i-1]+dp[2][i-1])%1000000009
    dp[1][i]=(dp[0][i-2]+dp[2][i-2])%1000000009
    dp[2][i]=(dp[0][i-3]+dp[1][i-3])%1000000009
for k in N:
    print((dp[0][k]+dp[1][k]+dp[2][k])%1000000009)
