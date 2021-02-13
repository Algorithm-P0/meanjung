"""
없어지는 시간이랑 q에 들어간 값이랑
시간이 뒤섞여서 틀린듯

import sys
from collections import deque

N, k = map(int, sys.stdin.readline().split())
graph = [list(map(int, list(sys.stdin.readline().strip())))]
graph.append(list(map(int, list(sys.stdin.readline().strip()))))


def bfs(y, x):
    q = deque()
    q.append([y, x])
    visited = [[y,x]]
    i = 0
    while q:
        y, x = q.popleft()
        if x>=N:
            return 1
        for [my, nx] in [[y, x+1], [y, x-1], [(-1)*y, x+k]]:
            if my==1:
                ny = 0
            else:
                ny = 1
            if 0<=nx<N and [my, nx] not in visited and graph[ny][nx]==1:
                q.append([my, nx])
                visited.append([my, nx])
            elif nx>=N and [my, nx] not in visited:
                q.appendleft([my, nx])
                visited.append([my, nx])
        if i>=N:
            continue
        graph[0][i]=0
        graph[1][i]=0
        i+=1
    return 0

print(bfs(1, 0))#y=1:위/ y=-1:아래
"""
import sys
from collections import deque

N, k = map(int, sys.stdin.readline().split())
lst1 = sys.stdin.readline().strip()
lst2 = sys.stdin.readline().strip()
lst = [lst1, lst2]
visited = [[False]*N for _ in range(2)]
visited[0][0]=True

def bfs():
    q = deque()
    q2 = deque()
    q2.append([0,0])
    remove = 0
    while q2:
        now_idx, lst_num = q2.popleft()
        if now_idx+1>=N or now_idx+k>=N:
            return 1
        if lst[lst_num][now_idx+1]=='1' and visited[lst_num][now_idx+1]==False:
            visited[lst_num][now_idx+1]=True
            q.append([now_idx+1, lst_num])
        if now_idx-1>remove and lst[lst_num][now_idx-1]=='1' and visited[lst_num][now_idx-1]==False:
            visited[lst_num][now_idx-1]=1
            q.append([now_idx-1, lst_num])
        if lst[(lst_num+1)%2][now_idx+k]=='1' and visited[(lst_num+1)%2][now_idx+k]==False:
            visited[(lst_num+1)%2][now_idx+k]=True
            q.append([now_idx+k, (lst_num+1)%2])
        if not q2:
            q2 = q
            q = deque()
            remove+=1
    return 0
print(bfs())