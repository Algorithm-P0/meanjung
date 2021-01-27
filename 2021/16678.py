import sys
N = int(sys.stdin.readline())
C = []
for _ in range(N):
    C.append(int(sys.stdin.readline()))
C.sort()
action = 0
max_honor = 1
for n in C:
    if n>=max_honor:
        action+=n-max_honor
        max_honor+=1
print(action)