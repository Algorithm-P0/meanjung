# 2751
import sys
# import sys로 입력받는 것이 시간이 덜 걸린다.
def merge(lst, start, mid, end):
    B=[]
    i=start
    j=mid+1
    while i<=mid and j<=end:
        if lst[i]<lst[j]:
            B.append(lst[i])
            i+=1
        else:
            B.append(lst[j])
            j+=1
    while i<=mid:
        B.append(lst[i])
        i+=1
    while j<=end:
        B.append(lst[j])
        j+=1
    b=0
    for k in range(start, end+1):
        lst[k]=B[b]
        b+=1
    
def merge_sort(lst, start, end):
    if(start<end):
        mid=int((start+end)/2)
        merge_sort(lst, start, mid)
        merge_sort(lst, mid+1,end)
        merge(lst, start, mid, end)


N=int(sys.stdin.readline())
numlist=[]
for _ in range(N):
    numlist.append(int(sys.stdin.readline()))
merge_sort(numlist, 0, N-1)
for i in numlist:
    print(i)

