import sys
# N세로선(x)  H가로선(y)
N, M, H = map(int, sys.stdin.readline().split())
if M==0:
    print(0)
    sys.exit()
bridge = [[0]*N for _ in range(H)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    bridge[a-1][b-1] = 1

def move():
    for start in range(N):
        x = start
        for y in range(H):
            if bridge[y][x]!=0:
                x+=1
            elif x>0 and bridge[y][x-1]!=0:
                x-=1
        if start!=x:
            return False
    return True

def dfs(cnt, idy, r):
    global ans
    if cnt==r:
        if move():
            ans = cnt
        return
    for y in range(idy, H):
        for x in range(N-1):
            if bridge[y][x]!=0:
                continue
            if x-1>=0 and bridge[y][x-1]!=0:
                continue
            if x+1<N and bridge[y][x+1]!=0:
                continue
            bridge[y][x]=1
            dfs(cnt+1, y, r)
            bridge[y][x]=0

ans = 4
flag = 1
for r in range(4):
    dfs(0, 0, r)
    if ans!=4:
        print(ans)
        flag = 0
        break
if flag!=0:
    print(-1)