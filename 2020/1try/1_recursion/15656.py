import sys
N, M =map(int, sys.stdin.readline().split())
Nlist=list(map(int, sys.stdin.readline().split()))

Nlist.sort()
out=[]
visited=[False]*N

def solve(depth, idx, N, M):
    if depth==M:
        print(' '.join(map(str, out)))
        return
    for i in range(idx, N):
        if visited[i]==False:
            visited[i]=True
            out.append(Nlist[i])
            solve(depth+1,i+1, N, M)
            out.pop()
            visited[i]=False
solve(0,0,N,M)