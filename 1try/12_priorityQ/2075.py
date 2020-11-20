import heapq
import sys

N = int(sys.stdin.readline())
heap = []
for n in map(int, sys.stdin.readline().split()):
    heapq.heappush(heap, n)
for _ in range(1, N):
    for n in map(int, sys.stdin.readline().split()):
        heapq.heappush(heap, n)
        heapq.heappop(heap)
print(heapq.heappop(heap))