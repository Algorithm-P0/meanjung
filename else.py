import heapq
import sys

lst = []
for l in map(int, sys.stdin.readline().split()):
    heapq.heappush(lst, l)

length1 = heapq.heappop(lst)
print(length1)
print(lst)