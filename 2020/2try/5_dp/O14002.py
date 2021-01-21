import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
dp = [0]*N
dp[0]=1
for i in range(1, N):
    for j in range(i-1,-1,-1):
        if A[i]>A[j]:
            if dp[i]<dp[j]:
                dp[i]=dp[j]
    dp[i]+=1
maxlen = max(dp)#가장 긴 길이
print(maxlen)

maxIdx = dp.index(maxlen)#가장 긴 길이의 인덱스
res=[A[maxIdx]]
maxIdx-=1
maxlen-=1
while maxIdx>=0:
    if dp[maxIdx]==maxlen:
        res.append(A[maxIdx])
        maxlen-=1
    maxIdx-=1
res.sort(reverse=False)
print(' '.join(map(str, res)))
