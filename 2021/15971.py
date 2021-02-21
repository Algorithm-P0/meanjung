import sys
n, a, b = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append([v, w])
    graph[v].append([u, w])
dist = [0]*(n+1)
maxi = [0]*(n+1)
visited = [0]*(n+1)
def dfs(v, d, m):
    dist[v] = d
    maxi[v] = m
    visited[v] = 1
    for i, w in graph[v]:
        if visited[i]==0:
            dfs(i, d+w, max(m, w))

if a==b:
    print(0)
else:
    dfs(a, 0, 0)
    print(dist[b]-maxi[b])