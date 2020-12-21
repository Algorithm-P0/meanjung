# 못품
import sys
from collections import deque
N, K = map(int, sys.stdin.readline().split())
C = list(map(int, sys.stdin.readline().split()))
C.sort(reverse=True)
if C[0]>(N+1)//2:
    print(-1)
else:
    result = deque()
    a = [0]*N
    for i in range(K):
        for j in range(C[i]):
            result.append(i+1)
    for i in range((N+1)//2):
        a[i*2] = result.popleft()
    pv = 1
    while len(result):
        a[pv] = result.popleft()
        pv+=2
    print(' '.join(map(str, a)))
