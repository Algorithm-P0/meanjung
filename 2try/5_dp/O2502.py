import sys
D,K=map(int, sys.stdin.readline().split())
dp=[[0,0] for _ in range(D+1)]
dp[1]=[1,0]
dp[2]=[0,1]
for i in range(3, D+1):
    dp[i][0]=dp[i-1][0]+dp[i-2][0]
    dp[i][1]=dp[i-1][1]+dp[i-2][1]
A, B = dp[D]
i = 1
while True:
    if (K-A*i)%B==0:
        break
    i+=1
print(i)
print((K-A*i)//B)