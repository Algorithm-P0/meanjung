def counting_sort(lst):
    counts=[0]*(max(lst)+1)
    for x in lst:
        counts[x]+=1    
    for i in range(len(counts)-1):
        counts[i+1]+=counts[i]
    res=[-1]*(len(lst))
    for i in range(len(lst)-1,-1,-1):
        counts[lst[i]]-=1
        res[counts[lst[i]]]=lst[i]
    for i in res:
        print(i)

import sys
numlist=[int(sys.stdin.readline())for _ in range(int(sys.stdin.readline()))]
counting_sort(numlist)