"""
에라토스테네스의 체
"""
import sys

Max = 1000000
prime = [False for _ in range(Max+1)]
for i in range(2, Max+1):
    if i*i>Max:
        break
    if prime[i]==False:
        for j in range(i*i, Max+1, i):
            prime[j]=True

while True:
    n = int(sys.stdin.readline())
    if n==0:
        break
    for i in range(2, Max+1):
        if prime[i]==False:
            j = n-i
            if prime[j]==False:
                print(n, '=', i, '+',j)
                break