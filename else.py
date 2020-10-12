import sys
n = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
cache=[[-1]*n for _ in range(n)]
def jump(y, x):
    if y>=n or x>=n:
        return 0
    if y==n-1 and x==n-1:
        return 1
    ret = cache[y][x]
    if ret!=-1:
        return ret
    jumpSize = board[y][x]
    return jump(y+jumpSize,x) or jump(y, x + jumpSize)
print(jump(0,0))