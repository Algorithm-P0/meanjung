def arrange(m, n, board):
    popSet = set()
    for x in range(1, m):
        for y in range(1, n):
            if board[y][x] == board[y-1][x-1] == board[y-1][x] == board[y][x-1] != '_':
                popSet |= set([(y,x), (y-1,x-1), (y-1,x), (y,x-1)])
    for y, x in popSet:
        board[y][x] = 0
    for i, row in enumerate(board):
        empty = ['_']*row.count(0)
        board[i] = empty + [block for block in row if block != 0]
    return len(popSet)

def solution(m, n, board):
    board = list(map(list, zip(*board)))
    count = 0
    while True:
        pop = arrange(m, n, board)
        if pop == 0:
            return count
        count += pop


solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"])