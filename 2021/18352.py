import sys
from collections import deque
N, M, K, X = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
visited = [False]*(N+1)
visited[X]=True
q = deque()
q.append([X,0])
answer = []
# 거리가 K를 넘어버리면 그 인덱스부터는 탐색 안해도 됨
while q:
    x, dist = q.popleft()
    if dist==K:
        answer.append(x)
    elif dist<K:
        for i in graph[x]:
            if visited[i]==False:
                visited[i]=True
                q.append([i,dist+1])
if len(answer)==0:
    print(-1)
else:
    answer.sort()
    for a in answer:
        print(a)