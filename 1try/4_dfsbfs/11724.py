import sys
N, M =map(int, sys.stdin.readline().split())
edges=[[] for _ in range(N+1)]
for _ in range(M):
    u, v=map(int, sys.stdin.readline().split())
    edges[u].append(v)
    edges[v].append(u)
"""
visited=[False]*(N+1)

def dfs(v):
    visited[v]=True
    for i in range(len(edges[v])):
        if visited[edges[v][i]]==False:
            dfs(edges[v][i])
cnt=0
for i in range(1,N+1):
    if visited[i]==False:
        cnt+=1
        dfs(i)
print(cnt)
"""
visited=[False]*(N+1)
def dfs(v):
    stack=[v]
    while stack:
        p=stack.pop()
        visited[p]=True
        for i in range(len(edges[p])):
            if visited[edges[p][i]]==False and edges[p][i] not in stack:
                stack.append(edges[p][i])
cnt=0
for i in range(1,N+1):
    if visited[i]==False:
        cnt+=1
        dfs(i)
print(cnt)