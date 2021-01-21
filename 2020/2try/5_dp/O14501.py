import sys
N = int(sys.stdin.readline())
TP=[[0,0]]
# TP[i][0] : 상담하는 데 필요한 기간
# TP[i][1] : 상담하고 받는 금액
dp=[0]*(N+1)
for _ in range(N):
    t, p = map(int, sys.stdin.readline().split())
    TP.append([t, p])
for i in range(N, 0, -1):
    mmax=[0]
    if i+TP[i][0]-1<=N:#날짜 계산
        dp[i]=TP[i][1]#금액
        for j in range(i+TP[i][0],N+1):
            mmax.append(dp[j])
        dp[i]+=max(mmax)
    else:
        for j in range(i+1, N+1):
            mmax.append(dp[j])
        dp[i]=max(mmax)
print(max(dp))

