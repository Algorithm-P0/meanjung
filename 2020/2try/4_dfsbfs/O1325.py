# 풀이는 쉬운데 시간초과가 관건. 어떻게 시간을 줄일 것인가?
# 시간초과 코드
import sys
N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[b].append(a)
# b를 해킹하면 a도 해킹할 수 있다.
cnt = [0]*(N+1) # i를 해킹했을 때 해킹할 수 있는 컴의 수 cnt[i]
def dfs(i):
    count = 0
    stack = [i]
    visited = [False]*(N+1)
    visited[i]=True
    while stack:
        x = stack.pop()
        count+=1
        for j in graph[x]:
            if visited[j]==False and j not in stack:
                stack.append(j)
                visited[j]=True
    cnt[i] = count
for i in range(1, N+1):
    if graph[i]:
        dfs(i)
m = max(cnt)
for i in range(1, N+1):
    if m == cnt[i]:
        print(i, end = " ")
"""
import sys
input = sys.stdin.readline # 중요!!!!, 입력 속도가 느리면 통과 불가능.
from collections import deque

# 너비 우선 탐색
def bfs(s):
    D = 0
    q = deque()
    q.append(s)
    visit = [0] * (N + 1)
    visit[s] = 1
    while q:
        here = q.popleft()
        D += 1
        for w in G[here]:
            if not visit[w]:
                visit[w] = 1
                q.append(w)
    return D # 방문한 정점의 수 D를 리턴한다.
                
N, M = map(int, input().split())
G = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    G[b].append(a)
mxd = 0
result = []
for i in range(1, N + 1):
    if G[i]:
        tmp = bfs(i) # 리턴값을 받아서 최대값과 비교
        if mxd <= tmp:
            if mxd < tmp:
                result = []
            mxd = tmp
            result.append(i)
print(*result)
"""