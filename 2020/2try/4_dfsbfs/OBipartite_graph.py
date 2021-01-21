import sys
from collections import deque
def bfs(start):
    q = deque()
    q.append(start)
    color[start]=-1
    while q:
        p = q.popleft()
        for i in graph[p]:
            if color[i]==0:
                color[i]=(-1)*color[p]
                q.append(i)
            elif color[i]==color[p]:
                return False # 이분그래프 틀리다.
    return True # 이분그래프 맞다.
T = int(sys.stdin.readline())
for _ in range(T):
    V, E = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(V+1)]
    color = [0]*(V+1)
    for _ in range(E):
        m,n = map(int, sys.stdin.readline().split())
        graph[m].append(n)
        graph[n].append(m)
    for i in range(1, V+1):
        if color[i]==0:
            ans = bfs(i)
            if ans == False: # 꼭 false부터 체크해야함
                break
    if ans == False:
        print('NOT Bipartite graph')
    else:
        print('Is Bipartitle graph')