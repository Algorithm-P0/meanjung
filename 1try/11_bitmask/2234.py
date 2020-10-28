# 참고 : https://pacific-ocean.tistory.com/401
# & 에서 이해가 안가는 부분이 있다.

import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
# n : 가로, m : 세로
castle = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
visited = [[0]*n for _ in range(m)]
result1, result2, result3 = 0, 0, 0

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def bfs(y, x):
    q = deque()
    q.append([y, x])
    visited[y][x]=1
    cnt = 1
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0<=ny<m and 0<=nx<n and visited[ny][nx]==0:
                if i==0:
                    if 1&castle[y][x]: # 값이 0이 나오면 해당 방향으로는 벽으로 막혀있지 않다.
                        # 0 => 막혀있지 않다.
                        # not 0 => 막혀있다. (조건문 만족)
                        continue
                elif i==1:
                    if 2&castle[y][x]:
                        continue
                elif i==2:
                    if 4&castle[y][x]:
                        continue
                elif i==3:
                    if 8&castle[y][x]:
                        continue
                visited[ny][nx]=1
                q.append([ny, nx])
                cnt+=1
    return cnt

for y in range(m):
    for x in range(n):
        if visited[y][x]==0:
            result1 += 1
            result2 = max(result2, bfs(y, x))
for y in range(m):
    for x in range(n):
        num = 1
        while num<9:
            if num&castle[y][x]:# 벽으로 막혀있다면
                visited = [[0]*n for _ in range(m)]
                castle[y][x]-=num
                result3 = max(result3, bfs(y, x))
                castle[y][x]+=num
            num*=2
print(result1)
print(result2)
print(result3)