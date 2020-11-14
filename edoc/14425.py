import sys
N, M = map(int, sys.stdin.readline().split())
S=[]
for _ in range(N):
    s = sys.stdin.readline().strip()
    S.append(s)
C = []
for _ in range(M):
    s = sys.stdin.readline().strip()
    C.append(s)
res=0
for c in C:
    if c in S:
        res+=1
print(res)