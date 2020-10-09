def func(A,B):
    if A==1 or B==1:
        return A*B
    GCD = -1
    for i in range(min(A,B),0,-1):
        if A%i==0 and B%i==0:
            GCD = i
            break
    if GCD == -1:
        return A*B
    return i*(A//i)*(B//i)

import sys
T = int(sys.stdin.readline())
for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    print(func(A, B))