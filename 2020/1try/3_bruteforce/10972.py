import sys
N=int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

i = N-1
while i>0 and arr[i-1]>arr[i]:
    i-=1
if i ==0:
    print(-1)
else:
    near=10001
    for j in range(i, N):
        if arr[i-1]<arr[j] and arr[j]<near:
            near = arr[j]
            nearIdx = j
    arr[i-1], arr[nearIdx] = arr[nearIdx], arr[i-1]
    s = arr[i:]
    s.sort()
    arr[i:]=s
    for k in arr:
        print(k, end=" ")

