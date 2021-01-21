import sys
import heapq

N, M, X = map(int, sys.stdin.readline().split())
# N명, M개의 간선, X번 마을에서 만나기
graph = [[] for _ in range(N+1)]
ans = [0]*(N+1)
def dijkstra(start, end):
    dist = [sys.maxsize]*(N+1)
    heap = []
    heapq.heappush(heap, [0, start])
    dist[start]=0
    while heap:
        w, now = heapq.heappop(heap)
        for next, weight in graph[now]:
            next_weight = weight + w
            if next_weight<dist[next]:
                dist[next]=next_weight
                heapq.heappush(heap, [next_weight, next])
    if start==end:
        for i in range(1, N+1):
            ans[i]+=dist[i]
    else:
        ans[start]+=dist[end]

for _ in range(M):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append([v, w])
for i in range(1, N+1):
    dijkstra(i, X)
print(max(ans))