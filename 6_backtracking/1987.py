# DFS / BFS
import sys
R, C = map(int, sys.stdin.readline().split())
board = [list(map(str, sys.stdin.readline().strip())) for _ in range(R)]
dx = [1,-1,0,0]
dy = [0,0,-1,1]

ans = 1
def DFS(x, y, cnt, passed):
    global ans
    ans = max(ans, cnt)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<R and 0<=ny<C:
            if board[nx][ny] not in passed:
                passed.append(board[ny][nx])
                DFS(nx, ny, cnt+1, passed)
                passed.pop()

DFS(0,0,1,[board[0][0]])
print(ans)