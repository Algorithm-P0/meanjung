import sys
N, M = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
nums.sort() # 오름차순 정렬

def solve(count, numList):
    if count==M:
        print(' '.join(map(str, numList)))
        return
    for i in range(N):
        if nums[i] not in numList:
            numList.append(nums[i])
            solve(count+1, numList)
            numList.pop()
solve(0, [])