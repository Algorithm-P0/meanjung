import sys

for i in sys.stdin.readlines():
    n, k = map(int, i.strip().split())
    chicken = n
    stamp = n
    while stamp>=k:
        chicken+=stamp//k
        stamp = stamp//k + stamp%k
    print(chicken)
