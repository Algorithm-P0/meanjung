import sys
from collections import deque
def bfs(y, x):
    q = deque()
    c = []
    q.append([y, x, 20])
    c.append([y, x, 20])
    while q:
        y, x, beer = q.popleft()
        if y==ry and x == rx:
            print("happy")
            return
        for ny, nx in d:
            if [ny, nx, 20] not in c:
                l = abs(nx-x)+abs(ny-y)
                if beer*50>=l:
                    q.append([ny,nx,20])
                    c.append([ny,nx,20])
    print("sad")
    return
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    hy, hx = map(int, sys.stdin.readline().split())
    d = []
    for _ in range(n):
        cy, cx = map(int, sys.stdin.readline().split())
        d.append([cy, cx])
    ry, rx = map(int, sys.stdin.readline().split())
    d.append([ry, rx])
    bfs(hy, hx)
