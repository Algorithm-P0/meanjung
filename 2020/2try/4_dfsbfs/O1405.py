import sys
N, E, W, S, M = map(int, sys.stdin.readline().split())
dx = [1,-1,0,0]
dy = [0,0,-1,1]
# E, W, S, N 순서
P = [E/100, W/100, S/100, M/100]
ans = 0
def dfs(y, x, k, prob, visited):
    global ans
    if k==N:
        if len(visited)==N+1:
            ans+=prob
        return
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if (ny, nx) not in visited:
            visited.append((ny, nx))
            dfs(ny, nx, k+1, prob*P[i], visited)
            visited.pop()
dfs(0,0,0,1,[(0,0)])
print('{:.10f}'.format(ans))