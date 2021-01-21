import sys
N = int(sys.stdin.readline())
W = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

def dfs(n, value, visited):
    global ans
    if len(visited)==N:
        k =W[visited[-1]][visited[0]] 
        if k!=0:
            ans = min(ans, value+k)
        return
    for i in range(N):
        if i not in visited and W[n][i]!=0:
            visited.append(i)
            dfs(i, value+W[n][i], visited)
            visited.pop()

ans = sys.maxsize
for i in range(N):
    dfs(i, 0, [i])
print(ans)