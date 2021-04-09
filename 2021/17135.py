# 다시 풀어보면 좋을듯
import sys

N, M, D = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

def shoot(y, position, copy_board):
    for d in range(1, D+1):
        for left in range(d, -1, -1):
            height = d-left
            if height>0 and 0<=y-height<N and 0<=position-left<M and copy_board[y-height][position-left]==1:
                return (y-height, position-left)
        for right in range(1, d):
            height = d-right
            if height>0 and 0<=y-height<N and 0<=position+right<M and copy_board[y-height][position+right]==1:
                return (y-height, position+right)
    return None

def simulation(positions):
    copy_board = [line[:] for line in board]
    killed = []
    for y in range(N, 0, -1):# 궁수들의 위치
        for position in positions:
            killed_enemy = shoot(y, position, copy_board)
            if killed_enemy==None:
                continue
            if killed_enemy not in killed:
                killed.append(killed_enemy)
        for (ly, lx) in killed:
            copy_board[ly][lx]=0
    return len(killed)

ans = 0
for i in range(M):
    for j in range(i + 1, M):
        for k in range(j + 1, M):
            ans = max(ans, simulation((i, j, k)))

print(ans)