import sys
T = int(sys.stdin.readline())
for _ in range(T):
    L, N = map(int, sys.stdin.readline().split())
    ant = [int(sys.stdin.readline()) for _ in range(N)]
    min_list = []
    max_list = []
    for a in ant:
        mmin = min(a, L-a)
        mmax = max(a, L-a)
        min_list.append(mmin)
        max_list.append(mmax)
    print(max(min_list), max(max_list))