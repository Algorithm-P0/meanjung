def bfs(x):
    q.append(x)
    colors[x]=1
    while q:
        x=q.pop(0)
        for nx in graph[x]:
            if colors[nx]==0: # 첫 방문
                q.append(nx)
                colors[nx]=(-1)*colors[x]
            elif colors[nx]==colors[x]:
                return 1
    return 0

import sys
v, e =map(int, sys.stdin.readline().split())
graph=[[] for _ in range(v+1)]
colors=[0]*(v+1)
q=[]
for _ in range(e):
    x,y=map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)
for i in range(1,v+1):
    if colors[i]==0:
        ans = bfs(i)
        if ans==1:
            break
if ans==1:
    print("NOT Bipartite graph")
else:
    print("IS Bipartite graph")
