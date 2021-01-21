# 후위 표기식
import sys
from collections import deque

N = int(sys.stdin.readline())
expression=deque()
expression.extend(list(map(str, sys.stdin.readline().strip())))
nums = []
for _ in range(N):
    nums.append(int(sys.stdin.readline()))
stack = []
while expression:
    p = expression.popleft()
    if p!='*' and p!='-' and p!='+' and p!='/':
        stack.append(nums[ord(p)-ord('A')])
        continue
    y = stack.pop()
    x = stack.pop()
    if p=='*':
        stack.append(x*y)
    elif  p=='-':
        stack.append(x-y)
    elif p=='+':
        stack.append(x+y)
    elif p=='/':
        stack.append(float(x/y))
print(format(stack[-1],".2f"))    
