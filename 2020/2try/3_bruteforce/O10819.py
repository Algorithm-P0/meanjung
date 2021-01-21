import sys
from itertools import permutations
N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
perms = list(permutations(nums, N))
ans = 0
for p in perms:
    s = 0
    for i in range(N-1):
        s += abs(p[i]-p[i+1])
    ans = max(ans, s)
print(ans)
