import sys
N, M = map(int, sys.stdin.readline().split())
nList = list(map(int, sys.stdin.readline().split()))
def solve(lst):
    if len(lst)==M:
        print(' '.join(map(str, lst)))
        return
    for i in range(N):
        lst.append(nList[i])
        solve(lst)
        lst.pop()
nList.sort()
for i in range(N):
    solve([nList[i]])
