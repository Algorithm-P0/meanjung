import sys
from collections import deque

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    L = list(map(int, sys.stdin.readline().split()))
    L.sort(reverse=True)
    S = deque()
    S.append(L[0])
    i = 1
    while i<N:
        S.appendleft(L[i])
        if i+1<N:
            S.append(L[i+1])
        i=i+2
    m = 0
    for k in range(N-1):
        m = max(m, abs(S[k+1]-S[k]))
    print(m)

"""
같은 해결 방안, 다른 코드
해결 방안 : 가장 큰 값을 가운데 넣고, 오른쪽 왼쪽 번갈아 놓기
< < < < > > > > 이런 식으로

그렇게 되면 서로 인접한 높이 차이가 
오름차순이나 내림차순 정렬을 했을 때의 한 개나 두 개 정도 차이가 된다.


A.sort()
result = 0
for j in range(2, N):
    c = A[j]-A[j-2]
    result = max(c, result)
print(result)

"""