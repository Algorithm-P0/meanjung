import sys
N = int(sys.stdin.readline())
f = [0]*(N+1)
g = [0]*(N+1)
f[0]=1
f[1]=2
g[0]=0
g[1]=1
for i in range(2, N+1):
    g[i] = ((f[i-1]+f[i-2])%1000000007+g[i-2])%1000000007
    f[i] = (2*g[i]%1000000007+f[i-2])%1000000007
print(f[N]%1000000007)