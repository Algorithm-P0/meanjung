import sys

N, M, V=map(int, sys.stdin.readline().split())
edges=[[] for _ in range(N+1)]
for _ in range(M):
    a,b=map(int, sys.stdin.readline().split())
    edges[a].append(b)
    edges[b].append(a)

for e in edges:
    e.sort()

visited=[False]*(N+1)
def dfs(v):
    print(v, end=" ")
    visited[v]=True
    for i in range(len(edges[v])):
        if visited[edges[v][i]]==False:
            dfs(edges[v][i])

def bfs(v):
    discovered=[False]*(N+1)
    q=[v]
    while q:
        p=q.pop(0)
        discovered[p]=True
        print(p, end=" ")
        for e in edges[p]:
            if discovered[e]==False and e not in q:
                q.append(e)
dfs(V)
print()
bfs(V)