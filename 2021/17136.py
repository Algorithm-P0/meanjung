# 다시 풀어보기
import sys
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(10)]
cnt = [0]*6
ans = sys.maxsize

def solve(y, x, c):
    global ans
    if y>=10:
        ans = min(ans, c)
        return
    if x>=10:
        solve(y+1, 0, c)
        return
    if graph[y][x]==1:
        for k in range(1, 6):
            if cnt[k]==5:
                continue
            if y+k-1>=10 or x+k-1>=10:
                continue
            flag = 0
            for ly in range(y, y+k):
                for lx in range(x, x+k):
                    if graph[ly][lx]==0:
                        flag = 1
                        break
                if flag==1:
                    break
            if flag==0:
                for ly in range(y, y+k):
                    for lx in range(x, x+k):
                        graph[ly][lx]=0
                cnt[k]+=1
                solve(y, x+k, c+1)
                cnt[k]-=1
                for ly in range(y, y+k):
                    for lx in range(x, x+k):
                        graph[ly][lx]=1
    else:
        solve(y, x+1, c)

solve(0, 0, 0)
if ans==sys.maxsize:
    print(-1)
else:
    print(ans)