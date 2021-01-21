# bfs + heap으로 풀기
import sys
import heapq

n = int(sys.stdin.readline())
room = [list(map(str, sys.stdin.readline().strip())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]
dy = [1,-1,0,0]
dx = [0,0,-1,1]
def dijkstra(y, x):
    heap = []
    heapq.heappush(heap, (0, y, x))
    visited[y][x]=True
    while heap:
        cnt, y, x = heapq.heappop(heap)
        if y==n-1 and x==n-1:
            return cnt
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<n and 0<=nx<n:
                if visited[ny][nx]==False:
                    visited[ny][nx]=True
                    if room[ny][nx]=='0':
                        room[ny][nx]='1'
                        heapq.heappush(heap, (cnt+1, ny, nx))
                    else:
                        heapq.heappush(heap, (cnt, ny, nx))
print(dijkstra(0,0))

"""
import sys
from collections import deque
n = int(sys.stdin.readline())
room = [list(map(str, sys.stdin.readline().strip())) for _ in range(n)]
count = [[-1]*n for _ in range(n)]
dy, dx = [1,-1,0,0], [0,0,-1,1]
def bfs():
    q = deque()
    q.append([0,0])
    count[0][0]=0
    while q:
        y, x = q.popleft()
        if y==n-1 and x==n-1:
            return count[y][x]
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<n and 0<=nx<n:
                if count[ny][nx]==-1:
                    if room[ny][nx]=='1':
                        count[ny][nx]=count[y][x]
                        q.appendleft([ny, nx])
                    elif room[ny][nx]=='0':
                        count[ny][nx]=count[y][x]+1
                        room[ny][nx]='1'
                        q.append([ny, nx])
print(bfs())
"""
