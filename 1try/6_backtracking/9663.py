# N-Queen
"""
오래걸린다 -> 더 빠른 시간복잡도를 갖는 풀이를 찾아보자💨
"""
import sys

N = int(sys.stdin.readline())

col = [False]*N
slash = [False]*(2*N-1)
backSlash = [False]*(2*N-1)
res=0
def dfs(i):
    global res
    if i==N:
        res+=1
        return
    for j in range(N):
        if col[j]==False and slash[i+j]==False and backSlash[N-1-i+j]==False:
            col[j]=slash[i+j]=backSlash[N-1-i+j]=True
            dfs(i+1)
            col[j]=slash[i+j]=backSlash[N-1-i+j]=False
dfs(0)
print(res)