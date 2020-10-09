# 스택
# 답은 맞음
# 시간초과, 메모리 초과
import sys
from collections import deque
string =sys.stdin.readline().strip()
q = deque()
length = 0
for i in range(len(string)):
    if string[i]!=')':
        q.append(string[i])
    else: # string[i]=='()
        cnt = 0
        while q:
            p = q.pop()
            if p == '(':
                x = q.pop()
                for i in range(int(x)*cnt):
                    q.append('1')
                break
            cnt+=1
print(len(q))


