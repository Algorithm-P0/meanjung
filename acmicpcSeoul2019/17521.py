import sys
n, W = map(int, sys.stdin.readline().split())
# n : 요일 수, W : 초기 현금
s=[]
for _ in range(n):
    s.append(int(sys.stdin.readline()))
for i in range(n-1):
    if s[i]<s[i+1]:
        x = W//s[i]
        W = W%s[i]
        W += x*s[i+1]
print(W)