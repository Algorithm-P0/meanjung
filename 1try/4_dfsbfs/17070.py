def dfs(x, y, z):
    global k
    if x==N-1 and y==N-1:
        k+=1
    if z==0 or z==2:
        if x+1<N:
            if D[y][x+1]==0:
                dfs(x+1, y, 0)
    if z==1 or z==2:
        if y+1<N:
            if D[y+1][x]==0:
                dfs(x, y+1, 1)
    if z==0 or z==1 or z==2:
        if x+1<N and y+1<N:
            if D[y][x+1]==0 and D[y+1][x]==0 and D[y+1][x+1]==0:
                dfs(x+1, y+1, 2)
import sys
N = int(sys.stdin.readline())
D = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
k = 0
dfs(1, 0, 0)
print(k)