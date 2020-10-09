import sys
N = int(sys.stdin.readline())
P=[0]
P.extend(list(map(int, sys.stdin.readline().split())))

if N==1:
    print(P[1])
else:
    dp=[0]*(N+1)
    dp[1]=P[1]
    for i in range(2, N+1):
        lst=[]
        dp[i]=P[i]
        for j in range(0, i+1):
            lst.append(dp[j]+P[i-j])
        dp[i]=max(lst)
    print(dp[N])