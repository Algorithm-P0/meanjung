import sys
import heapq

N = int(sys.stdin.readline())
heap = []
for _ in range(N):
    n = int(sys.stdin.readline())
    if n!=0:
        heapq.heappush(heap, (abs(n), n))
    else:
        try:
            print(heapq.heappop(heap)[1])
        except:
            print(0)