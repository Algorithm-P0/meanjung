import sys
from collections import deque

A, B = map(int, sys.stdin.readline().split())
stack = deque()
stack.append(A)
cnt = 0
while stack:
    cnt+=1
    ex = []
    while stack:
        x = stack.popleft()
        for i in (2*x, 10*x+1):
            if i<B:
                ex.append(i)
            elif i==B:
                print(cnt+1)
                sys.exit()
    stack.extend(ex)
if len(stack)==0:
    print(-1)
