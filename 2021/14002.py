import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

dp = [0]*N
dp[0]=1
for i in range(1, N):
    mmax = 0
    for j in range(i):
        if A[i]>A[j]:
            mmax = max(mmax, dp[j])
    dp[i]=mmax+1
maxlen = max(dp)
print(maxlen)

maxIdx = dp.index(maxlen)
res = [A[maxIdx]]
maxIdx -= 1
maxlen -= 1
while maxIdx>=0:
    if dp[maxIdx]==maxlen:
        res.append(A[maxIdx])
        maxlen-=1
    maxIdx-=1
res.sort()
print(' '.join(map(str, res)))
