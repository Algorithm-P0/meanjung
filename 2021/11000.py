import sys
import heapq
N = int(sys.stdin.readline())
C = []
heap = []
for i in range(N):
    C.append(list(map(int, sys.stdin.readline().split())))
C.sort()
for i in range(N):
    if len(heap)!=0 and heap[0]<=C[i][0]:
        heapq.heappop(heap)
    heapq.heappush(heap, C[i][1])
print(len(heap))
"""
시작시간이 빠른 순으로 정렬
반복문을 돌며
* i번째 반복문을 돈다고 가정하면,
i번째 강의의 시작시간보다 빨리 끝나는 시간이 heap에 없다면 i번째 강의의 종료시간 heap에 push
heap이니까 최소힙으로 자동정렬된다.
만약 i강의의 시작시간보다 빨리 끝나는 시간이 heap에 있다면 heappop
heappop은 heap에서 가장 빨리 끝나는 강의 종료시간을 의미한다.
그리고 마지막에 heappush로 사실상 update의미
"""