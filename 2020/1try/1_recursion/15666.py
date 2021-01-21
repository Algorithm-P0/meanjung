import sys
N, M = map(int, sys.stdin.readline().split())
nList=list(set(map(int, sys.stdin.readline().split())))
nList.sort()
def solve(depth, idx, lst):
    if depth==M:
        print(' '.join(map(str, lst)))
        return
    for i in range(idx, len(nList)):
        lst.append(nList[i])
        solve(depth+1, i, lst)
        lst.pop()
solve(0,0,[])