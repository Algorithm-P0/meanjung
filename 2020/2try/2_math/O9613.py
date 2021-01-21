import sys
from itertools import combinations
T = int(sys.stdin.readline())
def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

for _ in range(T):
    N = list(map(int, sys.stdin.readline().split()))
    combs = combinations(N[1:], 2)
    GCD=0
    for c in combs:
        c = list(c)
        GCD += gcd(c[1],c[0])
    print(GCD)