import sys
R, C = map(int, sys.stdin.readline().split())
alph = [list(sys.stdin.readline().strip()) for _ in range(R)]
dx = [1,-1,0,0]
dy = [0,0,-1,1]
"""
# 시간초과 -> 재귀때문인 듯
ans = 0
def dfs(y, x, alphabets):
    global ans
    ans = max(ans, len(alphabets))
    for i in range(4):
        lx = x + dx[i]
        ly = y + dy[i]
        if 0<=lx<C and 0<=ly<R:
            if alph[ly][lx] not in alphabets:
                alphabets.append(alph[ly][lx])
                dfs(ly, lx, alphabets)
                alphabets.pop()
dfs(0,0,[alph[0][0]])
print(ans)
"""
answer = 1
def BFS(y, x):
    global answer
    q = set([(y,x,alph[y][x])])
    while q:
        print(q)
        y, x, ans = q.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<C and 0<=ny<R and alph[ny][nx] not in ans:
                q.add((ny, nx, ans + alph[ny][nx]))
                answer = max(answer, len(ans)+1)
BFS(0,0)
print(answer)