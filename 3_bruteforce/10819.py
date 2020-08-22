# 말그대로 브루트포스 그 자체..
import sys
from itertools import permutations
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
perm = list(permutations(arr, N))
ans=0
for i in perm:
    sum=0
    for k in range(len(i)-1):
        sum+=abs(i[k+1]-i[k])
    ans=max(ans, sum)
print(ans)