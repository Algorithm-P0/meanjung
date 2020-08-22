import sys

N=int(sys.stdin.readline())
cost = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# cost[i][j] :  i에서 j로 가는 비용

ans = sys.maxsize

def dfs(start, next, value, visited):
    global ans

    if len(visited)==N:
        if cost[next][start]!=0:
            ans = min(ans, value+cost[next][start])
        return # 순환 못하는 것 거름
    
    for i in range(N):
        if cost[next][i]!=0 and i!=start and i not in visited:
            visited.append(i)
            dfs(start, i, value+cost[next][i], visited)
            visited.pop()

for i in range(N):
    dfs(i, i, 0, [i])
print(ans)