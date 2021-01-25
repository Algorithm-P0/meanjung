import sys
M, N = map(int, sys.stdin.readline().split())
candy=[]
M = -M
for _ in range(N):
    c = int(sys.stdin.readline())
    candy.append(c)
    M+=c
candy.sort()
ans = 0
for n in range(N):
    w = min(candy[n], M//(N-n))
    ans += (w*w)%(2**64)
    M -= w
print(ans%(2**64))