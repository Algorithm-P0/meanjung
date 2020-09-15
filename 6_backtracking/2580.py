import sys

def horizontal(x, val):
    if val in sudoku[x]:
        return False
    return True
def vertical(x, val):
    if val in sudoku[x]:
        return False
    return True
def square(x, y, val):
    nx = x//3 * 3
    ny = y//3 * 3
    for i in range(3):
        for j in range(3):
            if val == sudoku[nx+i][ny+j]:
                return False
    return True

def dfs(index):
    if index==len(zeros):
        print(sudoku)
        return
    else:
        for i in range(1,10):
            nx = zeros[index][0]
            ny = zeros[index][1]
            if horizontal(nx, i) and vertical(ny, i) and square(nx, ny, i):
                sudoku[nx][ny]=i
                dfs(index+1)
                sudoku[nx][ny]=0

sudoku = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
zeros = [(i,j) for i in range(9) for j in range(9) if sudoku[i][j]==0]
print(zeros)
dfs(0)