import sys
from collections import deque

T = int(sys.stdin.readline())
def bfs(y, x):
    q = deque()
    c = []
    q.append([y, x, 20])
    c.append([y, x, 20])
    while q:
        y, x, beer = q.popleft()
        if y==ry and x==rx:
            print("happy")
            break
        """
        d : 편의점 위치 리스트
        c : visited 역할
        """
        for ny, nx in d:
            if [ny,nx,20] not in c:
                l = abs(ny-y)+abs(nx-x)
                if beer*50>=l:
                    q.append([ny, nx, 20])
                    c.append([ny, nx, 20])
    print("sad")


for _ in range(T):
    n = int(sys.stdin.readline())
    hy, hx = map(int, sys.stdin.readline().split())
    d = []
    for _ in range(n):
        d.append(list(map(int, sys.stdin.readline().split())))
    ry, rx = map(int, sys.stdin.readline().split())
    d.append([ry, rx])
    bfs(hy, hx)