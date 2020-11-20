import sys
import heapq

N = int(sys.stdin.readline())
cards = []
for _ in range(N):
    heapq.heappush(cards, int(sys.stdin.readline()))
if len(cards)==1:
    print(0)
else:
    ans = 0
    while len(cards)>1:
        temp1 = heapq.heappop(cards)
        temp2 = heapq.heappop(cards)
        ans += temp1+temp2
        heapq.heappush(cards, temp1+temp2)
    print(ans)