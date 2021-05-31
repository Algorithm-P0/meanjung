import sys
from collections import deque

def solution(board):
    N = len(board)
    def bfs(start):
        dp = [[sys.maxsize] * N for _ in range(N)]
        #         위      왼      아래    오른
        dirs = [(-1,0), (0,-1), (1,0), (0,1)]
        q = deque([start])
        dp[0][0] = 0
        while q:
            y, x, cost, dirIdx = q.popleft()
            for i in range(4):
                ny = y + dirs[i][0]
                nx = x + dirs[i][1]
                if i != dirIdx:
                    ncost = cost + 600
                else:
                    ncost = cost + 100
                if 0<=ny<N and 0<=nx<N and board[ny][nx]==0 and dp[ny][nx]>ncost:
                    dp[ny][nx] = ncost
                    q.append((ny, nx, ncost, i))
        return dp[-1][-1]
    return min(bfs((0,0,0,2)), bfs((0,0,0,3)))



solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]])