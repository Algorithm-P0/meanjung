# https://algospot.com/judge/problem/read/MATCHORDER
# 출전 순서 정하기
def solve(Russia, Korea):
    Russia.sort()
    Korea.sort()
    win = 0
    for R in Russia:
        for i in range(len(Korea)):
            if R <= Korea[i]:
                win+=1
                Korea.pop(i)
                break
    return win

import sys
T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    Russia = list(map(int, sys.stdin.readline().split()))
    Korea = list(map(int, sys.stdin.readline().split()))
    print(solve(Russia, Korea))