import copy
import sys

def move(d):
    if d==0:
        for x in range(N):
            idx= 0
            for y in range(1, N):
                if board[y][x] != 0:
                    temp = board[y][x]
                    board[y][x] = 0
                    if board[idx][x] == 0:
                        board[idx][x] = temp
                    elif board[idx][x] == temp:
                        board[idx][x] = temp*2
                        idx+=1
                    else:
                        idx += 1
                        board[idx][x] = temp
    elif d==1:
        for x in range(N):
            idx = N-1
            for y in range(N-2, -1, -1):
                if board[y][x] != 0:
                    temp = board[y][x]
                    board[y][x] = 0
                    if board[idx][x] == 0:
                        board[idx][x] = temp
                    elif board[idx][x] == temp:
                        board[idx][x] = 2*temp
                        idx -= 1
                    else:
                        idx -= 1
                        board[idx][x] = temp

    elif d==2:
        for y in range(N):
            idx = 0
            for x in range(1, N):
                if board[y][x] != 0:
                    temp = board[y][x]
                    board[y][x] = 0
                    if board[y][idx] == 0:
                        board[y][idx] = temp
                    elif board[y][idx] == temp:
                        board[y][idx] = 2*temp
                        idx += 1
                    else:
                        idx += 1
                        board[y][idx] = temp

    else:
        for y in range(N):
            idx = N - 1
            for x in range(N-2, -1, -1):
                if board[y][x] != 0:
                    temp = board[y][x]
                    board[y][x] = 0
                    if board[y][idx] == 0:
                        board[y][idx] = temp
                    elif board[y][idx] == temp:
                        board[y][idx] = 2*temp
                        idx -= 1
                    else:
                        idx -= 1
                        board[y][idx] = temp




def dfs(cnt):
    global board, ans
    if cnt == 5:
        for y in range(N):
            for x in range(N):
                ans = max(ans, board[y][x])
        return
    cboard = copy.deepcopy(board)
    for i in range(4):
        move(i)
        dfs(cnt+1)
        board = copy.deepcopy(cboard)

N = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
ans = 0
dfs(0)
print(ans)
