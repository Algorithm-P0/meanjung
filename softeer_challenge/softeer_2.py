import sys

p,n = map(int, sys.stdin.readline().split())
a = list(map(int,sys.stdin.readline().split()))

tot = 0
for i in range(n):
    tot = ((tot*p)%1000000007 + a[i])%1000000007

print(tot%1000000007)