import sys
import heapq
N, E = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]

def dijkstra(start):
    dist = [sys.maxsize]*(N+1)
    dist[start]=0
    heap = []
    heapq.heappush(heap, [0, start])
    while heap:
        w, now = heapq.heappop(heap)
        for next, weight in graph[now]:
            next_weight = w + weight
            if next_weight<dist[next]:
                dist[next]=next_weight
                heapq.heappush(heap, [next_weight, next])
    return dist

for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([b, c])
    graph[b].append([a, c])
v1, v2 = map(int, sys.stdin.readline().split())
dist1 = dijkstra(1)
dist2 = dijkstra(v1)
dist3 = dijkstra(v2)
ans = min(dist1[v1]+dist2[v2]+dist3[-1], dist1[v2]+dist3[v1]+dist2[-1])
if ans<sys.maxsize:
    print(ans)
else:
    print(-1)