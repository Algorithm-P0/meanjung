import sys
N, M = map(int, sys.stdin.readline().split())
Nnums = list(map(int, sys.stdin.readline().split()))
Nnums.sort()
def solve(idx, lst):
    if len(lst)==M:
        print(' '.join(map(str, lst)))
        return
    for i in range(idx+1, N):
        lst.append(Nnums[i])
        solve(i, lst)
        lst.pop()
for i in range(N-M+1):
    solve(i, [Nnums[i]])