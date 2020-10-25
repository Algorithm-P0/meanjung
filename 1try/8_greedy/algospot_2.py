# https://algospot.com/judge/problem/read/LUNCHBOX
# 도시락 데우기
def solve(N):
    order=[]
    for i in range(N):
        order.append([-E[i], i]);
    order.sort()
    result = 0
    beginEat = 0
    for i in range(N):
        box = order[i][1]
        beginEat += M[box]
        result = max(result, beginEat+E[box])
    return result

import sys
T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    M = list(map(int, sys.stdin.readline().split()))
    E = list(map(int, sys.stdin.readline().split()))
    # 도시락 N개, M: 데우는 시간 , E: 먹는 시간
    print(solve(N))