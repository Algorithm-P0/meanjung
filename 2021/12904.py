import sys
S = list(sys.stdin.readline().strip())
T = list(sys.stdin.readline().strip())
while len(S)!=len(T):
    if T[-1]=='A':
        T.pop()
    else:
        T.pop()
        T = T[::-1]
if S==T:
    print(1)
else:
    print(0)

