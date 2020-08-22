def bfs(x):
    q.append(x)
    colors[x]=1
    while q:
        x = q.pop(0)
        for nx in a[x]:
            if colors[nx]==0:
                q.append(nx)
                colors[nx]=(-1)*colors[x]
            elif colors[nx]==colors[x]:
                return 1
    return 0

import sys
tc = int(sys.stdin.readline())
while tc:
    v, e = map(int, input().split())
    a = [[] for _ in range(v+1)]
    colors = [0 for _ in range(v+1)]
    q = []
    for _ in range(e):
        x, y = map(int, input().split())
        a[x].append(y)
        a[y].append(x)
    for i in range(1, v+1):
        if colors[i]==0:
            ans = bfs(i)
            if ans ==1:
                break
    if ans==1:
        print("NO")
    else:
        print("YES")
    tc -= 1