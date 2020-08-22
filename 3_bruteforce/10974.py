import sys
N = int(sys.stdin.readline())
arr = [i for i in range(1,N+1)]

def next_per(arr):
    i = N-1
    while i>0 and arr[i-1]>arr[i]:
        i-=1
    if i ==0:
        return False
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
        return True
while True:
    print(' '.join(map(str, arr)))
    if next_per(arr) is False:
        break

