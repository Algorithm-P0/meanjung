from collections import deque
import sys
n, m = map(int, sys.stdin.readline().split())
dx=[1,-1,0,0]
dy=[0,0,-1,1]
visit = [[[[False]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]
board = []
def move(y, x, dy, dx):
    c = 0
    while board[y+dy][x+dx]!='#' and board[y][x]!='O':
        y+=dy
        x+=dx
        c+=1
    return y, x, c
def bfs():
    while q:
        r_y, r_x, b_y, b_x, d = q.popleft()
        if d>10:
            break
        for i in range(4):
            nr_y, nr_x, rc = move(r_y, r_x, dy[i], dx[i])
            nb_y, nb_x, bc = move(b_y, b_x, dy[i], dx[i])
            if board[nb_y][nb_x]!='O':
                if board[nr_y][nr_x]=='O':
                    print(d)
                    return
                if nr_y==nb_y and nr_x==nb_x:
                    if rc>bc:
                        nr_y-=dy[i]
                        nr_x-=dx[i]
                    else:
                        nb_y-=dy[i]
                        nb_x-=dx[i]
                if not visit[nr_y][nr_x][nb_y][nb_x]:
                    visit[nr_y][nr_x][nb_y][nb_x]=True
                    q.append([nr_y, nr_x, nb_y, nb_x, d+1])
    print(-1)
for y in range(n):
    b=list(sys.stdin.readline().strip())
    board.append(b)
    for x in range(m):
        if b[x]=='R':
            r_y, r_x = y, x
        if b[x]=='B':
            b_y, b_x = y, x
q = deque()
q.append([r_y, r_x, b_y, b_x, 1])
visit[r_y][r_x][b_y][b_x]=True
bfs()