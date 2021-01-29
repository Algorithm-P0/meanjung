import sys
D, K = map(int, sys.stdin.readline().split())
dp = [[0,0],[1,0],[0,1]]
for i in range(3, 31):
    dp.append([dp[i-1][0]+dp[i-2][0], dp[i-1][1]+dp[i-2][1]])
"""
# 시간초과
flag = 0
for b in range(1,K+1):
    for a in range(1, b+1):
        if dp[D][0]*a + dp[D][1]*b == K:
            print(a)
            print(b)
            flag = 1
            break
    if flag==1:
        break
"""
A = dp[D][0]
B = dp[D][1]
i = 1
while True:
    if (K-A*i)%B==0:
        break
    i+=1
print(i)
print((K-A*i)//B)