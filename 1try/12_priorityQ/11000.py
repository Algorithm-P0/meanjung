"""
복습하기
"""
import sys
import heapq

N = int(sys.stdin.readline())
lec = []
for _ in range(N):
    s, t = map(int, sys.stdin.readline().split())
    lec.append([s, t])
lec.sort()
heap = []
heapq.heappush(heap, lec[0][1])#처음 시작하는 강의의 끝나는 시간
for i in range(1, N):
    start, end = lec[i][0], lec[i][1]
    if heap[0]>start:# 끝나는 시간이 다음 강의 시작하는 시간보다 나중이라면
        heapq.heappush(heap, end)# 강의실 추가
    else:
        heapq.heappop(heap)
        heapq.heappush(heap, end)
print(len(heap))