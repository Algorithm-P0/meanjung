import sys

N, M = map(int, sys.stdin.readline().split())
friends=[[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    friends[a].append(b)
    friends[b].append(a)

visited=[False for _ in range(N)]

def dfs(v, depth):
    global ans
    visited[v]=True
    if depth>=4:
        ans = True
        return
    for nxt in friends[v]:
        if not visited[nxt]:
            dfs(nxt, depth+1)
            visited[nxt]=False

ans=False
for i in range(N):
    dfs(i,0)
    visited[i]=False
    if ans:
        break
print(1 if ans else 0)