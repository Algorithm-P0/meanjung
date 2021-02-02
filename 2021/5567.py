import sys
from collections import deque
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
friend = []
q = deque()
for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    graph[i].append(j)
    graph[j].append(i)
    if i==1:
        friend.append(j)
        q.append(j)
    elif j==1:
        friend.append(i)
        q.append(i)
while q:
    p = q.popleft()
    for i in graph[p]:
        if i not in friend and i not in q:
            friend.append(i)
print(len(friend)-1)