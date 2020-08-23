import sys
C=int(sys.stdin.readline())
stairs=[0]*301
dp=[0]*301
for i in range(1,C+1):
    stairs[i]=int(sys.stdin.readline())
dp[1]=stairs[1]
dp[2]=dp[1]+stairs[2]
for i in range(3,C+1):
    dp[i]=max(dp[i-3]+stairs[i-1]+stairs[i], dp[i-2]+stairs[i])
print(dp[C])