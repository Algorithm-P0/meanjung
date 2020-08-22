import sys
import itertools

N, S = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
comb = []
for i in range(1,N+1):
    comb.extend(list(itertools.combinations(num,i)))
ans = 0
for k in comb:
    if sum(k)==S:
        ans+=1
print(ans)
