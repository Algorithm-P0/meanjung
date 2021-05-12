from collections import deque

def solution(board, moves):
    H = len(board) # 높이
    W = len(board[0]) # 너비
    boardQueue = [deque() for _ in range(W)]
    for w in range(W):
        for h in range(H-1, -1, -1):
            if board[h][w]==0:
                break
            boardQueue[w].append(board[h][w])

    basketStack = []
    ans = 0
    for m in moves:
        if boardQueue[m-1]:
            popVal = boardQueue[m-1].pop()
            if basketStack:
                if basketStack[-1] == popVal:
                    basketStack.pop()
                    ans += 2
                    continue
        basketStack.append(popVal)
    return ans

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

solution(board, moves)