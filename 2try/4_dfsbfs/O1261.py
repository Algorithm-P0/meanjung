import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
miro = [list(map(int, sys.stdin.readline().strip())) for _ in range(M)]
visited = [[-1]*N for _ in range(M)]
dx = [-1,1,0,0]
dy = [0,0,1,-1]
q = deque()
q.append([0,0])
visited[0][0]=0
while q:
    y, x = q.popleft()
    if y==M-1 and x==N-1:
        break
    for i in range(4):
        ly = y + dy[i]
        lx = x + dx[i]
        if 0<=ly<M and 0<=lx<N:
            if visited[ly][lx]==-1: # 방문하지 않았다면 방문하기
                if miro[ly][lx]==0: # 빈 방이라면
                    visited[ly][lx]=visited[y][x] 
                    q.appendleft([ly,lx]) # 빈 방이니까 큐의 맨 앞에 넣어주기
                else: # 벽이라면
                    visited[ly][lx]=visited[y][x]+1 # 벽 하나 더 부숨
                    q.append([ly,lx])
print(visited[-1][-1])
"""
생각해보면 visited!=-1 일 때,
min(visited[ly][lx], visited[y][x]) 이 필요할 것 같다.
하지만 빈 방일 때 appendleft를 해줌으로써
visited값을 최소로 해 줄 수 있다.
"""
