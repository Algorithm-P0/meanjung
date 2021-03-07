import sys
n, m, h = map(int, sys.stdin.readline().split())
bridge = [[False]*n for _ in range(h)]
# 세로선 n개/ 가로선 h개
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    bridge[a-1][b-1]=True
def check():
    for x in range(n):
        k = x # 세로선
        for y in range(h):
            if bridge[y][k]:
                k+=1
            elif k>0 and bridge[y][k-1]:
                k-=1
        if x!=k:
            return False
    return True
def dfs(cnt, y, x):
    global ans
    if check():
        ans = min(ans, cnt)
        return
    elif cnt==3 or ans<=cnt:
        return
    for i in range(y, h):# 가로선
        if i==y:
            k = x
        else:
            k = 0
        for j in range(k, n-1):# 세로선
            if bridge[i][j]==False and bridge[i][j+1]==False:
                bridge[i][j]=True
                dfs(cnt+1, i, j+2)
                bridge[i][j]=False

    
ans = 4
dfs(0,0,0)
if ans<4:
    print(ans)
else:
    print(-1)