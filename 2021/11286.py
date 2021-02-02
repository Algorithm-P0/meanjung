# 절대값이 가장 작은 수 출력, 제거
# 절대값이 가장 작은 수가 여러개이면 가장 작은 수 출력, 제거
# 비어있을때 출력해야 한다면 0
import sys
import heapq
N = int(sys.stdin.readline())
heap = []
for _ in range(N):
    x = int(sys.stdin.readline())
    if x!=0:
        heapq.heappush(heap, [abs(x),x])
    else:
        try:
            y = heapq.heappop(heap)
            print(y[1])
        except:
            print(0)