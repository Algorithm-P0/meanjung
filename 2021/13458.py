import sys
import math
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B, C = map(int, sys.stdin.readline().split())
ms, ss = N, 0
for i in range(N):
    A[i]-=B
    if A[i]>0:
        ss+=math.ceil(A[i]/C)
print(ms+ss)