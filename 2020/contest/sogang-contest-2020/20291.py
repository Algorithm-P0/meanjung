import sys
N = int(sys.stdin.readline())
ext = {}
for _ in range(N):
    e = (sys.stdin.readline().strip()).split('.')[1]
    if e in ext.keys():
        ext[e] += 1
    else:
        ext[e] = 1
res = sorted(ext.items())
for r in res:
    print(' '.join(map(str, r)))