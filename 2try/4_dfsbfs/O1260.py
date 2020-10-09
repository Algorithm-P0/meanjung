import sys
from collections import deque
N, M, V = map(int, sys.stdin.readline().split())
graph=[[] for _ in range(N+1)]
for _ in range(M):
    v, w = map(int, sys.stdin.readline().split())
    graph[v].append(w)
    graph[w].append(v)
for g in graph:
    g.sort()

visited = [False]*(N+1)
visited[0]=True
"""
# DFS -> 재귀
def DFS(v):
    if visited[v]==False:
        visited[v]=True
        print(v, end=" ")
        for g in graph[v]:
            if visited[g]==False:
                DFS(g)
DFS(V)
"""
# DFS -> 스택
def DFS_stack(v):
    s = [v]
    res=[]
    while s:
        p = s.pop()
        visited[p]=True
        if p not in res:
            res.append(p)
        for i in range(len(graph[p])-1,-1,-1):
            if visited[graph[p][i]]==False:
                s.append(graph[p][i])
    print(' '.join(map(str, res)))
DFS_stack(V)

# BFS
discovered = [False]*(N+1)
def BFS(v):
    q = deque()
    q.append(v)
    discovered[v]=True
    res=[]
    while q:
        p = q.popleft()
        res.append(p)
        for g in graph[p]:
            if discovered[g]==False:
                q.append(g)
                discovered[g]=True
    print(' '.join(map(str, res)))
BFS(V)