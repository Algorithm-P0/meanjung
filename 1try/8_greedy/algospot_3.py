# https://algospot.com/judge/problem/read/STRJOIN
# 문자열 합치기
import sys
import heapq

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    strlist = []
    ans = 0
    for i in map(int, sys.stdin.readline().split()):
        heapq.heappush(strlist, i)
    for _ in range(N-1):
        length1 = heapq.heappop(strlist)
        length2 = heapq.heappop(strlist)
        ans += length1 + length2
        heapq.heappush(strlist, length1+length2)
    print(ans)