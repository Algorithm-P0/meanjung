# https://deok2kim.tistory.com/48
from collections import deque
def solution(n, path, order):
    answer = True
    adj = {n: [] for n in range(n)}
    for s, e in path:
        adj[s].append(e)
        adj[e].append(s)
    precedeA = {}
    precedeB = {}

    for a, b in order:
        precedeA[a]=b
        precedeB[b]=a
        if b==0:
            return False
        if a==0:
            precedeA[0]=0
    visited = [0]*n
    visited[0]=1

    q = deque()
    q.append(0)
    while q:
        current = q.popleft()
        if current == precedeA.get(precedeB.get(current)):
            visited[current]=2
        else:
            for neighbor in adj[current]:
                if visited[neighbor] == 0:
                    q.append(neighbor)
                    visited[neighbor]=1
                    if precedeA.get(neighbor):
                        if visited[precedeA[neighbor]]==2:
                            q.append(precedeA[neighbor])
                            visited[precedeA[neighbor]]=1
                        precedeA[neighbor]=0
    for i in visited:
        if i==0:
            return False
    return answer




solution(9, [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]], [[8,5],[6,7],[4,1]])