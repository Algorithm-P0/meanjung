import sys
from itertools import combinations

N=int(sys.stdin.readline())
people = [x for x in range(N)]
capability = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
res = float('inf')

for c in combinations(people, N//2):
    start = list(c)
    link = list(set(people)-set(c))
    start_comb = list(combinations(start, 2))
    link_comb = list(combinations(link, 2))
    start_sum=0
    for x,y in start_comb:
        start_sum+=(capability[x][y]+capability[y][x])
    link_sum=0
    for x, y in link_comb:
        link_sum+=(capability[x][y]+capability[y][x])
    if res>abs(start_sum-link_sum):
        res = abs(start_sum-link_sum)
print(res)