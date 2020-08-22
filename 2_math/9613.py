def combination(arr):
    res = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            res.append([arr[i], arr[j]])
    return res

def GCD(A ,B):
    for i in range(min(A,B),0,-1):
        if A%i==0 and B%i==0:
            return i


import sys

t = int(sys.stdin.readline())
for _ in range(t):
    lst = list(map(int, sys.stdin.readline().split()))
    com = combination(lst[1:])
    res=0
    for k in range(len(com)):
        res+=GCD(com[k][0], com[k][1])
    print(res)