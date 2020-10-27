# 에라토스테네스의 체
import sys
N, K = map(int, sys.stdin.readline().split())
# 2-N 까지의 정수, K번째 지우는 수 구하기
primes = [0]*1001
primes[0], primes[1] = 1,1
for i in range(2, N+1):
    j = 1
    while i*j<=N:
        if primes[i*j]==0:
            primes[i*j]=1
            K-=1
            if K==0:
                break
        j+=1
    if K==0:
        break
print(i*j)