import sys
import heapq

inf = sys.maxsize
city_count = int(sys.stdin.readline())
bus_count = int(sys.stdin.readline())
graph= [[] for _ in range(city_count+1)]
dist = [inf]*(city_count+1)
heap =[]
def dijkstra(start, end):
    dist[start]=0
    heapq.heappush(heap, [0, start])
    while heap:
        w, now = heapq.heappop(heap)
        for next, weight in graph[now]:
            next_weight = weight+w
            if next_weight<dist[next]:
                dist[next]=next_weight
                heapq.heappush(heap, [next_weight, next])
    return dist[end]

for _ in range(bus_count):
    u, v, c = map(int, sys.stdin.readline().split())
    graph[u].append([v, c])

start_city, arrive_city = map(int, sys.stdin.readline().split())
print(dijkstra(start_city, arrive_city))