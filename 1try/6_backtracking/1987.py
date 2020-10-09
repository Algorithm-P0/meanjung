import sys
R, C = map(int, sys.stdin.readline().split())
board = [list(map(str, sys.stdin.readline().strip())) for _ in range(R)]
dx = [0,0,-1,1]
dy = [1,-1,0,0]
answer = 1
def BFS(y, x):
    global answer
    q = set([(y,x,board[y][x])])
    while q:
        y, x, ans = q.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<C and 0<=ny<R and board[ny][nx] not in ans:
                q.add((ny, nx, ans + board[ny][nx]))
                answer = max(answer, len(ans)+1)
BFS(0,0)
print(answer)
"""
answer = 1
passed=[board[0][0]]
def DFS(y, x, ans):
    global answer
    answer = max(ans, answer)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<C and 0<=ny<R:
            if board[ny][nx] not in passed:
                passed.append(board[ny][nx])
                DFS(ny, nx, ans+1)
                passed.remove(board[ny][nx])
DFS(0,0,answer)
print(answer)
"""