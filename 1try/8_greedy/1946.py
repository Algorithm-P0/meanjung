import sys
T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    L = []
    for _ in range(N):
        a, b = map(int, sys.stdin.readline().split())
        L.append([a, b])
    L.sort()
    cnt = 1
    mmin = L[0][1]
    for i in range(1, N):
        if mmin>L[i][1]:
            mmin = L[i][1]
            cnt+=1
    print(cnt)
