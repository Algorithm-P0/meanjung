"""
import sys
N = int(sys.stdin.readline())
nums = []
for _ in range(N):
    nums.append(int(sys.stdin.readline()))
nums.sort(reverse=True)
ans = 0
while len(nums)!=1:
    x = nums.pop()
    y = nums.pop()
    ans += (x+y)
    nums.append(x+y)
    nums.sort(reverse=True)
print(ans)
# 시간초과가 발생한다.
# while문을 돌면서 sort를 해서 시간초과가 난다.
# 그렇다면 sort의 시간복잡도를 줄일 순 없을까?
"""
# 해결책 heapq
import sys
import heapq
N = int(sys.stdin.readline())
nums = []
for _ in range(N):
    heapq.heappush(nums, int(sys.stdin.readline()))
ans = 0
while len(nums)!=1:
    x = heapq.heappop(nums)
    y = heapq.heappop(nums)
    ans+=(x+y)
    heapq.heappush(nums, x+y)
print(ans)