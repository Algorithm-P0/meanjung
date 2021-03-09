"""
5번 cctv 먼저 모두 처리
1-4번 cctv를 bruteforce로 처리 - 방향의 중복순열 구하기
하나씩 move하면서 cctv로 가릴 수 있는 개수 체크
"""
import sys
from collections import deque
from copy import deepcopy

N, M = map(int, sys.stdin.readline().split())
# 세로N 가로M
dy = [-1,0,1,0]
dx = [0,1,0,-1]
cctv = []
cctv5 = []
graph = []
area = N*M #사각지대
for i in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    graph.append(row)
    for j in range(M):
        if graph[i][j]==5:
            cctv5.append([i, j])
            area-=1
        elif 0<graph[i][j]<5:
            cctv.append([i, j])
            area-=1
        elif graph[i][j]==6:
            area-=1

for i in range(len(cctv5)):
    y, x = cctv5[i]
    for i in range(4):
        ny, nx = y, x
        while True:
            ny += dy[i]
            nx += dx[i]
            if not 0<=ny<N or not 0<=nx<M or graph[ny][nx]==6:
                break
            if 0<graph[ny][nx]<6 or graph[ny][nx]==-1:
                continue
            graph[ny][nx]=-1
            area-=1

def move(y, x, d):
    cnt = 0
    while True:
        ny = y + dy[d]
        nx = x + dx[d]
        if not 0<=ny<N or not 0<=nx<M or copy_graph[ny][nx]==6:
            return cnt
        if 0<copy_graph[ny][nx]<6 or copy_graph[ny][nx]==-1:
            y, x = ny, nx
            continue
        copy_graph[ny][nx]=-1
        cnt+=1
        y, x = ny, nx

def dfs(cnt):
    global ans, copy_graph
    if cnt==len(cctv):
        copy_graph = deepcopy(graph)
        c = 0
        for i in range(len(cctv)):
            y, x = cctv[i]
            if graph[y][x]==1:
                c+=move(y, x, dir[i])
            elif graph[y][x]==2:
                c+=move(y, x, dir[i])
                c+=move(y, x, (dir[i]+2)%4)
            elif graph[y][x]==3:
                c+=move(y, x, dir[i])
                c+=move(y, x, (dir[i]+1)%4)
            elif graph[y][x]==4:
                c+=move(y, x, dir[i])
                c+=move(y, x, (dir[i]+1)%4)
                c+=move(y, x, (dir[i]+2)%4)
        ans = min(ans, area-c)
        return
    for i in range(4):
        dir.append(i)
        dfs(cnt+1)
        dir.pop()

dir = deque()
ans = area
dfs(0)
print(ans)