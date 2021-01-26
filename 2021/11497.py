import sys
from collections import deque
T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    L = list(map(int, sys.stdin.readline().split()))
    L.sort(reverse=True)
    S = deque()
    S.append(L[0])
    for i in range(1, N, 2):
        S.appendleft(L[i])
        if i+1<N:
            S.append(L[i+1])
    m = abs(S[0]-S[-1])
    for i in range(N-1):
        m = max(m, abs(S[i+1]-S[i]))
    print(m)