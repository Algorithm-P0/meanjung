"""
# 시간초과
import sys
N = int(sys.stdin.readline())
c = list(map(int, sys.stdin.readline().split()))
graph = [[0]*N for _ in range(N)]
for i in range(N-1):
    graph[i+1][i] = c[i]
for i in range(2, N):
    for j in range(i-2, -1, -1):
        graph[i][j] = graph[i-1][j]*graph[i][i-1]
res = 0
for g in graph:
    res+=sum(g)%int(1e9+7)
print(res%int(1e9+7))
"""
import sys
N = int(sys.stdin.readline())
c = list(map(int, sys.stdin.readline().split()))
MOD = int(1e9+7)
prev = 0
ans = 0
for i in range(N-1):
    prev = ((prev+1)*c[i])%MOD
    ans += prev
    ans = ans%MOD
print(ans)
