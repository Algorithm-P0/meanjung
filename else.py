# dp
# https://solved.ac/problems/tags/dp?sort=level&direction=asc&page=2

# dfs/bfs
# 시뮬레이션/구현
# https://solved.ac/problems/tags/implementation?sort=level&direction=asc&page=9
# https://www.acmicpc.net/problem/2564
import heapq
heap = [[3,3],[3,-3],[1,1], [1,-1], [2,-2], [2,2]]
heapq.heapify(heap)
while heap:
    print(heapq.heappop(heap))
#print(heap)