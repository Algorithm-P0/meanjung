import sys
N, M = map(int, sys.stdin.readline().split())
lab = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dy = [-1,1,0,0]
dx = [0,0,-1,1]
virus = []
for y in range(N):
    for x in range(N):
        if lab[y][x]==1:
            lab[y][x]='-'#벽
        elif lab[y][x]==2:
            virus.append([y, x])#바이러스
            lab[y][x] = '*'
        elif lab[y][x]==0:
            lab[y][x]=-1#빈칸

def spread_time(lst):
    t = 0
    lab_copy = [l[:] for l in lab]
    for y, x in lst:
        lab_copy[y][x]=0
    while True:
        # 가능한 모든 칸에 바이러스가 다 차있으면 break
        # 바이러스 퍼트리기
        flag = 1
        for y in range(N):
            for x in range(N):
                if lab_copy[y][x]==-1:
                    flag = 0
                    break
            if flag==0:
                break
        if flag==0 and len(lst)==0:
            return -1
        if flag==1:
            return t
        re_virus = []
        while lst:
            y, x = lst.pop()
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0<=ny<N and 0<=nx<N:
                    if lab_copy[ny][nx]==-1 or lab_copy[ny][nx]=='*':
                        lab_copy[ny][nx] = lab_copy[y][x]+1
                        re_virus.append([ny,nx])
        lst = re_virus
        t+=1

time = sys.maxsize

def dfs(idx, virus_M):# virus combination
    global time
    if len(virus_M)==M:
        s = spread_time(virus_M)
        if s!=-1:
            time = min(time, s)
        return
    for i in range(idx+1, len(virus)):
        if virus[i] not in virus_M:
            virus_M.append(virus[i])
            dfs(i, virus_M)
            virus_M.pop()

for i in range(len(virus)-M+1):
    dfs(i, [virus[i]])
if time==sys.maxsize:
    print(-1)
else:
    print(time)

# 오류 찾기