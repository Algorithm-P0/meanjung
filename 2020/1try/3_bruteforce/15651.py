# 내장함수 itertools.product
import sys
import itertools
N,M=map(int, sys.stdin.readline().split())
lst = [i for i in range(1,N+1)]
perms = list(itertools.product(lst, repeat=M))
for p in perms:
    print(' '.join(list(map(str, p))))
