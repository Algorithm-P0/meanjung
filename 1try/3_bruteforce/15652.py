import sys
import itertools

N, M =map(int, sys.stdin.readline().split())
lst = range(1, N+1)
combs = list(itertools.combinations_with_replacement(lst, M))
for c in combs:
    print(' '.join(map(str,c)))