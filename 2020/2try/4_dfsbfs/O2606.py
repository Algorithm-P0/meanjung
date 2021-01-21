import sys
N = int(sys.stdin.readline())
P = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]
for _ in range(P):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False]*(N+1)
visited[1]=True
stack = [1]
cnt = -1
while stack:
    x = stack.pop()
    cnt+=1
    for i in graph[x]:
        if visited[i]==False and i not in stack:
            stack.append(i)
            visited[i]=True
print(cnt)
