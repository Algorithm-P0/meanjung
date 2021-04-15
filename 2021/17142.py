"""
# 시간초과
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
lab = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dy = [-1,1,0,0]
dx = [0,0,-1,1]
virus = []
empty_space = []
for y in range(N):
    for x in range(N):
        if lab[y][x]==1:
            lab[y][x]='-'#벽
        elif lab[y][x]==2:
            virus.append([y, x])#바이러스
            lab[y][x] = '*'
        elif lab[y][x]==0:
            lab[y][x]=-1#빈칸
            empty_space.append([y, x])

def spread_virus(active_virus):
    # init
    lab_copy = [l[:] for l in lab]
    empty_space_copy = [i for i in empty_space]
    q = deque()
    for y, x in active_virus:
        lab_copy[y][x]=0
        q.append([y, x, 0])
    rt = 0
    # spread
    while q:
        if len(empty_space_copy)==0:
            return rt
        y, x, t = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<N and 0<=nx<N:
                if lab_copy[ny][nx]=='*':#빈칸
                    lab_copy[ny][nx]=t+1
                    q.append([ny, nx, t+1])
                    rt = t+1
                elif lab_copy[ny][nx]==-1:#빈칸
                    lab_copy[ny][nx]=t+1
                    q.append([ny, nx, t+1])
                    empty_space_copy.remove([ny, nx])
                    rt = t+1

    return -1
        
ans = sys.maxsize
def dfs(idx, lst):# virus combination
    global ans
    if len(lst)==M:
        active_virus = lst # [[0,0],[1,5],[4,3]]
        res = spread_virus(active_virus)
        if res!=-1:
            ans = min(ans, res)
        return
    for i in range(idx+1, len(virus)):
        if virus[i] not in lst:
            lst.append(virus[i])
            dfs(i, lst)
            lst.pop()

for i in range(len(virus)-M+1):
    dfs(i, [virus[i]])

if ans==sys.maxsize:
    print(-1)
else:
    print(ans)
    """
import sys
from collections import deque
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())
lab = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dy = [-1,1,0,0]
dx = [0,0,-1,1]
virus = deque()
for y in range(N):
    for x in range(N):
        if lab[y][x]==2:
            virus.append([y, x])
ans = []
def bfs(virus_list):
    dist = [[-1]*N for _ in range(N)]
    q = deque()
    for pos in virus_list:
        q.append(pos)
        dist[pos[0]][pos[1]]=0
    max_dist = 0
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=nx<N and 0<=ny<N and lab[ny][nx]!=1 and dist[ny][nx]==-1:
                dist[ny][nx] = dist[y][x]+1
                if lab[ny][nx]==0:
                    max_dist = max(max_dist, dist[ny][nx])
                q.append([ny, nx])
    a = list(sum(dist, []))
    if a.count(-1)==list(sum(lab, [])).count(1):
        ans.append(max_dist)

for now_virus_list in combinations(virus, M):
    bfs(now_virus_list)
print(min(ans) if ans else -1)