import sys
A, B =map(int,sys.stdin.readline().split())

for i in range(min(A,B),0,-1):
    if A%i == 0 and B%i == 0:
        break
print(i) # 최대 공약수
print(i*(A//i)*(B//i))