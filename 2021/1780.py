import sys
N = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
ans = [0, 0, 0]
#      0, 1, -1
def solve(y, x, l):
    if l==1:
        ans[graph[y][x]]+=1
        return
    flag = 0
    for i in range(y, y+l):
        for j in range(x, x+l):
            if graph[y][x]!=graph[i][j]:
                flag = 1
                break
        if flag==1:
            break
    if flag==0:
        ans[graph[y][x]]+=1
        return
    else:
        for ny in range(y, y+l, l//3):
            for nx in range(x, x+l, l//3):
                solve(ny, nx, l//3)
solve(0,0,N)
print(ans[-1])
print(ans[0])
print(ans[1])