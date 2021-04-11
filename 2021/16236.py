"""
# 하나의 예제만 통과가 안된다..
import sys
from collections import deque
N = int(sys.stdin.readline())
ocean = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
size = 2
for y in range(N):
    for x in range(N):
        if ocean[y][x]==9:
            ocean[y][x]=0
            sy, sx = y, x
            break
dy = [-1,0,0,1]
dx = [0,-1,1,0]
eat = 0
# 가장 가까이 있는 먹을 수 있는 물고기 찾기
def findFish(sy, sx, size):
    q = deque()
    q.append([sy, sx, 0])
    visited = [[False]*N for _ in range(N)]
    visited[sy][sx]=True
    while q:
        y, x, time = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<N and 0<=nx<N:
                if visited[ny][nx]==False:
                    if ocean[ny][nx]==0 or ocean[ny][nx]==size:
                        q.append([ny,nx,time+1])
                        visited[ny][nx]=True
                    elif ocean[ny][nx]<size:#먹어버리기
                        ocean[ny][nx]=0
                        return ny, nx, time+1
                    else:
                        continue
    return False
time = 0
while True:
    k = findFish(sy, sx, size)
    if k==False:
        print(time)
        break
    sy, sx, t = k[0], k[1], k[2]
    eat+=1
    if eat==size:
        eat = 0
        size+=1
    time+=t 
"""
from collections import deque
import sys

input = sys.stdin.readline
dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]

def bfs(y, x, weight, time, eat):
    q, can_eat = deque(), []
    q.append([y, x])
    c = [[-1]*n for _ in range(n)]
    c[y][x] = time
    while q:
        qlen = len(q)
        while qlen:
            y, x = q.popleft()
            for i in range(4):
                ny = y + dx[i]
                nx = x + dy[i]
                if 0 <= ny < n and 0 <= nx < n:
                    if c[ny][nx] == -1:
                        if ocean[ny][nx] == 0 or ocean[ny][nx] == weight:
                            c[ny][nx] = c[y][x] + 1
                            q.append([ny, nx])
                        elif 0 < ocean[ny][nx] < weight:
                            can_eat.append([ny, nx])
            qlen -= 1

        if can_eat:
            ny, nx = min(can_eat)
            eat += 1
            if eat == weight:
                eat = 0
                weight += 1
            ocean[ny][nx] = 0
            return ny, nx, weight, c[y][x] + 1, eat

    print(time)
    sys.exit()

n = int(input())
ocean = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if ocean[i][j] == 9:
            y, x = i, j
            ocean[i][j] = 0

weight, time, eat = 2, 0, 0
while True:
    y, x, weight, time, eat = bfs(y, x, weight, time, eat)