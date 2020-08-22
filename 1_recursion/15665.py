import sys
N, M = map(int, sys.stdin.readline().split())
nList=list(set(map(int, sys.stdin.readline().split())))
nList.sort()

def func(depth, lst):
    if depth==M:
        print(' '.join(map(str, lst)))
        return
    for i in range(len(nList)):
        lst.append(nList[i])
        func(depth+1, lst)
        lst.pop()
func(0,[])
