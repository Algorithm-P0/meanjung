import sys
N = int(sys.stdin.readline())
A=list(map(int, sys.stdin.readline().split()))
if N==1:
    print(A[0])
else:
    m = min(A)
    if m<0:
        idx = A.index(m)
        A.pop(idx)
    dp=[0]
    dp.extend([ x for x in A ])
    for i in range(1,len(A)+1):
        dp[i] = max(dp[i], dp[i-1]+A[i-1])
    print(max(dp))