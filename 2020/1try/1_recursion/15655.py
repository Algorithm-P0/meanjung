import sys
N, M=map(int, sys.stdin.readline().split())
Nlist=list(map(int, sys.stdin.readline().split()))
Nlist.sort()
out=[]
visited=[False]*N
def solve(depth, N, M):
    if depth==M:
        print(' '.join(map(str, out)))
        return
    for i in range(N):
        if Nlist[i] not in out and visited[i]==False:
            visited[i]=True
            out.append(Nlist[i])
            solve(depth+1, N, M)
            out.pop()
            visited[i]=False
solve(0,N,M)
"""
# (성공한) 내 풀이
import sys
N, M =map(int, sys.stdin.readline().split())
nList=list(map(int, sys.stdin.readline().split()))
nList.sort()

def solve(depth, idx, lst):
    if depth==M:
        print(' '.join(map(str, lst)))
        return
    if idx<N:
        lst.append(nList[idx])
        solve(depth+1, idx+1, lst)
        lst.pop()
        solve(depth, idx+1, lst)
solve(0,0,[])
"""