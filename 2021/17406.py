import sys
from collections import deque
N, M, K = map(int, sys.stdin.readline().split())
# 가로N, 세로M, 회전연산K
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
f = []
for _ in range(K):
    r, c, s = map(int, sys.stdin.readline().split())
    f.append([r-1, c-1, s])
visited = [0]*K
q = deque()
ans = sys.maxsize
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
def rotate(q):
    copy_A = [a[:] for a in A]
    copy_q = deque([l[:] for l in q])
    while copy_q:
        r, c, s = copy_q.popleft()
        ly, lx, ry, rx = r-s, c-s, r+s, c+s
        while True:
            if ly>=ry and lx>=rx:
                break
            dir = 0
            y, x, before = ly, lx, copy_A[ly][lx]
            while True:
                ny = y + dy[dir]
                nx = x + dx[dir]
                if not lx<=nx<=rx or not ly<=ny<=ry:
                    dir += 1
                    continue
                temp = copy_A[ny][nx]
                copy_A[ny][nx] = before
                before = temp
                y, x = ny, nx
                if [y, x] == [ly, lx]:
                    ly += 1
                    lx += 1
                    ry -= 1
                    rx -= 1
                    break
    t = sys.maxsize
    for row in copy_A:
        t = min(t, sum(row))
    return t

def permutation(cnt):# 회전연산의 순열 구하기
    global ans
    if cnt==K:
        ans = min(ans, rotate(q))
        return
    for i in range(K):
        if visited[i]==0:
            visited[i]=1
            q.append(f[i])
            permutation(cnt+1)
            visited[i]=0
            q.pop()
permutation(0)
print(ans)