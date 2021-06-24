import sys
# K번의 행동 E동 W서 S남 N북
K, E, W, S, N = map(int, sys.stdin.readline().split())
d = [E/100, W/100, S/100, N/100]
dy = [0,0,-1,1]
dx = [1,-1,0,0]
res = 0
def solve(p, visited, y, x):
    global res
    if len(visited)==K+1:
        res+=p
        return
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if (ny, nx) not in visited:
            visited.append((ny,nx))
            solve(p*d[i], visited, ny, nx)
            visited.pop()

solve(1, [(0,0)], 0, 0)
print('{:.10f}'.format(res))
