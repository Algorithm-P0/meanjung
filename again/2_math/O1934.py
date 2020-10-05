import sys
T = int(sys.stdin.readline())
def LCS(a, b): # 최대공약수
    mmin = min(a,b)
    mmax = max(a,b)
    for i in range(1, mmin+1):
        if mmin%i==0 and mmax%i==0:
            lcs = i
    return lcs
for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())
    print((a*b)//LCS(a,b))
