import sys
N = int(sys.stdin.readline())
height = list(map(int, sys.stdin.readline().split()))
result = [0]*N
for i in range(N):
    count = 0
    for j in range(N):
        if result[j]==0 and count==height[i]:
            result[j]=i+1
            break
        if result[j]==0:
            count+=1
print(' '.join(map(str, result)))