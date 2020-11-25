import sys
A, B = map(int, sys.stdin.readline().split())
n = int(sys.stdin.readline())
N = list(map(int, sys.stdin.readline().split()))
num = 0
for i in range(n):
    num+=(A**i)*N[n-1-i]
res = []
while num!=0:
    res.append(num%B)
    num = num//B
print(*res[::-1])