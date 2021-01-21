import sys
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
flag = 'YES'
for i in range(N):
    if i%2 == arr[i]%2:
        flag = 'NO'
        break
print(flag)