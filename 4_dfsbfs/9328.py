# 꼭 다시 풀어보기

import sys
from collections import deque

dx=[1,-1,0,0]
dy=[0,0,-1,1]

def bfs():
    de = deque()
    de.append([0,0])
    ch[0][0]=0
    dq = [deque() for _ in range(26)] # dp[i]: i 열쇠가 있을때 들어갈 수 있는 문의 배열
    r=0
    while de:
        x, y = de.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<h+2 and 0<=ny<w+2:
                if a[nx][ny]=='*': # 벽 -> 아무것도 못함
                    continue
                if ch[nx][ny]==-1: # 한 번도 방문 안한 지점만 방문
                    ch[nx][ny]=0 # 방문했다 표시
                    if a[nx][ny]=='$': # 문서 -> 훔치기
                        r+=1 # 훔치는 개수 + 1
                    elif 'A'<=a[nx][ny]<='Z': # 문
                        d = ord(a[nx][ny])-ord('A')
                        if alp[d]==False: # 해당 문의 열쇠가 없다면
                            dq[d].append([nx,ny]) # 열쇠가 없으니 들어가진 못하고 일단 저장
                            continue
                    elif 'a'<=a[nx][ny]<='z': # 열쇠
                        k = ord(a[nx][ny])-ord('a')
                        alp[k]=True # 열쇠 획득
                        while dq[k]: # 열쇠가 있으니 들어갈 수 있다
                            kx, ky = dq[k].popleft()
                            de.append([kx, ky])
                    de.append([nx,ny])
    return r

T = int(sys.stdin.readline())
for _ in range(T):
    h, w = map(int, sys.stdin.readline().split())
    a = [list('.'*(w+2))]
    for i in range(h):
        a.append(list('.'+sys.stdin.readline().strip()+'.'))
    a.append(list('.'*(w+2)))
    k = sys.stdin.readline().strip()

    ch=[[-1]*(w+2) for _ in range(h+2)]
    alp = [False]*26 # 키

    if k!='0':
        for i in k:
            alp[ord(i)-ord('a')]=True # 어떤 키를 갖고있나
    print(bfs())