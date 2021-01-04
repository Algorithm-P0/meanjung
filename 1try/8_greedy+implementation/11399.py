import sys
N = int(sys.stdin.readline())
P = list(map(int, sys.stdin.readline().split()))
P.sort()
sum = 0
for p in P:
    sum+=p*N
    N=N-1
print(sum)