import sys
N, M = map(int, sys.stdin.readline().split())
nList=list(map(int, sys.stdin.readline().split()))
nList.sort()
def solve(depth, lst):
    if depth==M:
        print(' '.join(map(str, lst)))
        return
    for i in range(N):
        if nList[i] not in lst:
            lst.append(nList[i])
            solve(depth+1, lst)
            lst.pop()
solve(0,[])