import sys

N, M=map(int, sys.stdin.readline().split())
Nlist=list(map(int, sys.stdin.readline().split()))
Nlist.sort()
out=[]
res=[]
visited=[False]*N
def solve(depth, N, M):
    if depth==M:
        ss=' '.join(map(str, out))
        if ss not in res:
            print(ss)
            res.append(ss)
        return
        print(' '.join(map(str, out)))
    for i in range(N):
        if visited[i]==False:
            visited[i]=True
            out.append(Nlist[i])
            solve(depth+1, N, M)
            visited[i]=False
            out.pop()
solve(0,N,M)