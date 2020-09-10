import sys
N=int(sys.stdin.readline())
P=[0]
P.extend(list(map(int, sys.stdin.readline().split())))

if N==1:
    print(P[1])
else:
    dp=[0]*(N+1)
    dp[1]=P[1]
    for i in range(2, N+1):
        dp[i]=P[i]
        lst=[]
        for j in range(i+1):
            lst.append(dp[j]+P[i-j])
        dp[i]=min(lst)
    print(dp[N])
