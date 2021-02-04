import sys
n, m = map(int, sys.stdin.readline().split())
# 세로n 가로m
arr = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(n)]
ans = 0
for y in range(n):
    for x in range(m):
        if y>0 and x >0 and arr[y][x]==1:
            arr[y][x] = 1+min(arr[y-1][x], arr[y][x-1], arr[y-1][x-1])
        ans = max(ans, arr[y][x])
print(ans**2)