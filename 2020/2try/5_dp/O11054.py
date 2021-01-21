import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
# 수열의 처음부터 최대 증가 수열
LIS = [0]*N
LIS[0]=1
for i in range(1, N):
    m = 0
    for j in range(i-1,-1,-1):
        if A[i]>A[j] and m<LIS[j]:
            m = LIS[j]
    if m == 0:
        LIS[i] = 1
    else:
        LIS[i] = m+1

reverse_LIS = [0]*N
reverse_LIS[N-1]=1
for i in range(N-1,-1,-1):
    m = 0
    for j in range(N-1,i,-1):
        if A[i]>A[j] and m<reverse_LIS[j]:
            m = reverse_LIS[j]
    if m==0:
        reverse_LIS[i]=1
    else:
        reverse_LIS[i]=m+1
ans = 0
for i in range(N):
    k = LIS[i]+reverse_LIS[i]-1
    if ans<k:
        ans = k
print(ans)
