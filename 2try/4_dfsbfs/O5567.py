import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
stack = []
f = []
for i in graph[1]:
    stack.append(i)
    f.append(i)
while stack:
    p = stack.pop()
    for i in graph[p]:
        if i not in f and i not in stack and i!=1:
            f.append(i)
print(len(f))

