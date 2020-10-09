# 복습할 필요가 있겠다..
import sys
from collections import deque
N, K = map(int, sys.stdin.readline().split())
ch = [[-1,0] for _ in range(100001)]
d = deque()
d.append(N)
ch[N][0]=0
ch[N][1]=1
while d:
    x = d.popleft()
    for i in (x+1, x-1, x*2):
        if 0<=i<100001:
            if ch[i][0]==-1: #처음 방문
                ch[i][0]=ch[x][0]+1
                ch[i][1]=ch[x][1]
                d.append(i)
            elif ch[i][0]==ch[x][0]+1: #재방문인데 하나 차이나는 경우
                ch[i][1]+=ch[x][1]
print(ch[K][0])
print(ch[K][1])