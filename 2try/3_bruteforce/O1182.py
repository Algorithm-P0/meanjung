# 부분수열이란, 원소가 연속하지 않게 뽑는 경우도 포함하는 용어이다.
import sys
N, S = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
cnt=0
def solve(idx, lst):
    global cnt
    if sum(lst)==S:
        cnt+=1
    # 여기서 return 해주면 N=3, S=0, nums=[1,-1,0] 일때 답이 다르다.
    for i in range(idx+1, N):
        lst.append(nums[i])
        solve(i, lst)
        lst.pop()
for i in range(N):
    solve(i, [nums[i]])
print(cnt)