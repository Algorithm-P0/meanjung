import sys
import itertools
N=int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B=[ j for j in A]
operator_count = list(map(int, sys.stdin.readline().split()))
operator=[]
for i in range(4):
    if operator_count[i]!=0:
        if i==0:
            op = '+'
        elif i==1:
            op ='-'
        elif i==2:
            op='*'
        else:
            op='%'
        operator.extend([op]*operator_count[i])
opperm = list(itertools.permutations(operator, N-1))
mmin = 1000000000
mmax = -1000000000
for p in opperm:
    k=0
    for i in p:
        if i=='+':
            B[k+1]=B[k]+B[k+1]
        elif i=='-':
            B[k+1]=B[k]-B[k+1]
        elif i=='*':
            B[k+1]=B[k]*B[k+1]
        else:
            B[k+1]=int(B[k]/B[k+1])
        k+=1
    mmin = min(mmin, B[-1])
    mmax = max(mmax, B[-1])
    B = [ j for j in A]
print(mmax)
print(mmin)