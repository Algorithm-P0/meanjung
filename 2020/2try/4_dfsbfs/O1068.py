import sys
from collections import deque

N = int(sys.stdin.readline())
P = list(map(int, sys.stdin.readline().split()))
D = int(sys.stdin.readline())
graph = [[] for _ in range(N)]
for i in range(N):
    if P[i]!=-1:
        graph[P[i]].append(i)
for i in range(N):
    if D in graph[i]:
        graph[i].remove(D)
def bfs(D):
    visited = [False]*N
    q = deque()
    q.append(D)
    visited[D]=True
    while q:
        x = q.popleft()
        for i in graph[x]:
            if visited[i]==False and i not in q:
                visited[i]=True
                q.append(i)
        graph[x]=-1
bfs(D)
cnt=0
for g in graph:
    if type(g)==list and len(g)==0:
        cnt+=1
print(cnt)