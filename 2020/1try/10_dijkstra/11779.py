import sys
import heapq

n = int(sys.stdin.readline()) # 도시 개수
m = int(sys.stdin.readline()) # 버스 개수
graph = [[] for _ in range(n+1)]
dist = [sys.maxsize]*(n+1)
for _ in range(m):
    start, end, cost = map(int, sys.stdin.readline().split())
    graph[start].append([end, cost])
A, B = map(int, sys.stdin.readline().split())
trace = [0]*(n+1)
def dijkstr(A, B):
    heap = []
    heapq.heappush(heap, [0, A])
    dist[A]=0
    while heap:
        w, now = heapq.heappop(heap)
        for next, weight in graph[now]:
            next_weight = weight+w
            if next_weight<dist[next]:
                dist[next]=next_weight
                trace[next]=now
                heapq.heappush(heap, [next_weight, next])
    return dist[B]

print(dijkstr(A, B))

count = 0
path = [B]
tmp = trace[B]
while tmp!=0:
    path.append(tmp)
    tmp = trace[tmp]
print(len(path))
print(*path[::-1])
