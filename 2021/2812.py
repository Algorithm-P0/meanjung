import sys
N, K = map(int, sys.stdin.readline().split())
number = list(sys.stdin.readline().strip())
t = []
tk = K
for i in range(N):
    while tk>0 and len(t)!=0 and t[-1]<number[i]:
        del t[-1]
        tk -= 1
    t.append(number[i])
print(''.join(t[:N-K]))