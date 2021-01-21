import sys
from collections import deque
S = sys.stdin.readline().strip()
SS = []
zero, one = 0, 0
for s in S:
    SS.append(s)
    if s=='0':
        zero+=1
    else:
        one+=1
zero = zero//2
one = one//2
SSS= []
for i in range(len(SS)):
    if one>0 and SS[i] == '1':
        one-=1
        continue
    SSS.append(SS[i])
result = deque()
for i in range(len(SSS)-1,-1,-1):
    if zero>0 and SSS[i]=='0':
        zero-=1
        continue
    result.appendleft(SSS[i])
print(''.join(result))
