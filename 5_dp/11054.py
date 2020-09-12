# 놀랍게도 맞는 풀이,, 다들 이렇게 풀었더라
import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
updp=[1]*N
dwdp=[1]*N
for i in range(N):
    for j in range(i):
        if A[i]>A[j]:
            updp[i]=max(updp[i], updp[j]+1)
for i in range(N-1,-1,-1):
    for j in range(N-1,i-1,-1):
        if A[i]>A[j]:
            dwdp[i]=max(dwdp[i], dwdp[j]+1)
res=0
for i in range(N):
    updp[i]=updp[i]+dwdp[i]-1
    if res<updp[i]:
        res=updp[i]
print(res)