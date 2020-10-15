# 이해가 잘 안간다...

import sys
N = int(sys.stdin.readline())
nums=list(map(int, sys.stdin.readline().split()))
stack = []
result = [-1]*N
stack.append(0)
for i in range(1, N):
    while stack and nums[stack[-1]]<nums[i]:
        result[stack[-1]]=nums[i]
        stack.pop()
    stack.append(i)
print(' '.join(map(str, result)))