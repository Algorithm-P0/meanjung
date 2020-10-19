import sys
from collections import deque
dy = [-1,1,0,0]
dx = [0,0,-1,1]
def bfs():
    de = deque()
    de.append([0,0])
    visited[0][0]=0 # 아무데서나 시작해도 되니까 임의로 0,0에서 시작
    dq = [deque() for _ in range(26)] # door_q
    docs = 0 # 훔치는 문서 개수
    while de:
        y, x = de.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0<=ny<h+2 and 0<=nx<w+2:
                if maps[ny][nx]=='*': # 벽이면 아무것도 할 수 없음
                    continue
                if visited[ny][nx]==-1: # 방문하지 않았다면
                    visited[ny][nx]=0 # 방문했다 표시
                    if maps[ny][nx]=='$': # 문서획득
                        docs+=1
                    elif 'A'<=maps[ny][nx]<='Z': # 문
                        d = ord(maps[ny][nx])-ord('A') # 해당 문에 해당하는 열쇠 idx
                        if keys[d]==False: # 해당 문에 해당하는 열쇠가 없다
                            dq[d].append([ny, nx])
                            """
                            door_q에 문 위치 저장
                            door_q[0]은 a열쇠가 있어야 열 수 있는 문 A의 위치들 저장
                            """
                            continue
                    elif 'a'<=maps[ny][nx]<='z': # 열쇠
                        k = ord(maps[ny][nx])-ord('a')
                        keys[k]=True
                        while dq[k]: # 해당 열쇠로 열 수 있는 문 다 열기
                            ky, kx = dq[k].popleft()
                            de.append([ky, kx]) # 문 열었으니까 접근가능 -> de에 위치 저장
                    de.append([ny, nx])
    return docs
T = int(sys.stdin.readline())
for _ in range(T):
    h, w = map(int, sys.stdin.readline().split())
    # h: 높이, w: 가로
    maps = [list('.'*(w+2))]
    for _ in range(h):
        maps.append(list('.'+sys.stdin.readline().strip()+'.'))
    maps.append(list('.'*(w+2)))
    k = sys.stdin.readline().strip()
    visited = [[-1]*(w+2) for _ in range(h+2)]
    keys = [False]*26
    if k!='0':
        for i in k:
            keys[ord(i)-ord('a')]=True
    print(bfs())