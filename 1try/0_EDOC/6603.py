"""
import sys
import itertools

while True:
    klist=list(map(int, sys.stdin.readline().split()))
    if klist[0]==0:
        break
    com=list(itertools.combinations(klist[1:],6))
    for c in com:
        for i in c:
            print(i, end=" ")
        print()
    print()
"""
import sys

def lotto(x, cnt):
    if cnt==6:
        for i in range(k):
            if select[i]==True:
                print(klist[i], end=" ")
        print()
        return
    
    for i in range(x, k):
        select[i]=True
        lotto(i+1, cnt+1)
        select[i]=False


while True:
    klist=list(map(int, sys.stdin.readline().split()))
    k=klist[0]
    if k==0:
        break
    select=[0 for _ in range(k)]
    klist=klist[1:]
    lotto(0,0)
    print()
