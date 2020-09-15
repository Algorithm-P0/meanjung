# 조합문제 -> 백트래킹으로 풀어보기
import sys
N, M = map(int, sys.stdin.readline().split())
"""
1-N 까지의 자연수 중 중복없이 M개를 고른 수열
을 모두 구하라
"""
def solve(lst):
    if len(lst)==M:
        print(' '.join(map(str, lst)))
        return
    for j in range(1, N+1):
        if j not in lst:
            lst.append(j)
            solve(lst)
            lst.pop()

for i in range(1, N+1):
    solve([i])