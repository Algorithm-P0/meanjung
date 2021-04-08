import sys
N = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
ans = 0
def solve(ey, ex, d):
    global ans
    if ey==N-1 and ex==N-1:
        ans+=1
        return
    if d==0 or d==2:
        #가로
        if 0<=ex+1<N:
            if graph[ey][ex+1]==0:
                solve(ey, ex+1, 0)
    if d==1 or d==2:
        #세로
        if 0<=ey+1<N:
            if graph[ey+1][ex]==0:
                solve(ey+1, ex, 1)
    if d==0 or d==1 or d==2:
        #대각선
        if 0<=ey+1<N and 0<=ex+1<N:
            if graph[ey+1][ex]==0 and graph[ey][ex+1]==0 and graph[ey+1][ex+1]==0:
                solve(ey+1, ex+1, 2)
solve(0, 1, 0)
print(ans)