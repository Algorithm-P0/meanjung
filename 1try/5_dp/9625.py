import sys
K=int(sys.stdin.readline())
f=[[1,0],[0,1]]
for _ in range(K-1):
    f.append([f[-1][1], f[-1][0]+f[-1][1]])
print(*f[K])