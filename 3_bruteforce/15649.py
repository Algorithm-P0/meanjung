import sys
import itertools
N, M = map(int, sys.stdin.readline().split())
Nlist=[i for i in range(1, N+1)]
perms = itertools.permutations(Nlist, M)
for p in perms:
    p = list(p)
    print(' '.join(map(str, p)))