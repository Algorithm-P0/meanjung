import sys
import heapq
inf = 1000000000
V, E = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline())

graph = [[] for _ in range(V+1)]
dist = [inf]*(V+1)
heap = []
def dijkstra(start):
    dist[start]=0
    heapq.heappush(heap, [0, start])
    while heap:
        w, now = heapq.heappop(heap)
        # start에서 now까지의 최단 거리 : w
        for next, weight in graph[now]:
            # now에 인접한 vertex의 idx : next, now->vertex까지의 가중치 : weight
            next_weight = weight + w
            if next_weight<dist[next]:
                dist[next]=next_weight
                heapq.heappush(heap, [next_weight, next])
# 최소힙을 만들어주므로 start와 가장 가까운 vertex부터 탐색할 수 있다.
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append([v, w])
dijkstra(start)
for i in dist[1:]:
    if i==inf:
        print("INF")
    else:
        print(i)
