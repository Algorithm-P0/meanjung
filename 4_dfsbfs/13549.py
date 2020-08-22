# 수빈 : N, 동생 : K
"""
deque 쓰는 게 메모리는 좀 더 들지만
시간은 덜 든다.
"""
import sys
from collections import deque
N, K =map(int, sys.stdin.readline().split())
visited=[False]*100001
time=[0]*100001
#q=[N]
q=deque()
q.append(N)
visited[N]=True
while q:
    #x=q.pop(0)
    x=q.popleft()
    if x==K:
        break
    if 0<=2*x<=100000 and visited[2*x]==False:
        #q.insert(0, 2*x)
        q.appendleft(2*x)
        visited[2*x]=True
        time[2*x]=time[x]
    if 0<=x+1<=100000 and visited[x+1]==False:
        q.append(x+1)
        visited[x+1]=True
        time[x+1]=time[x]+1
    if 0<=x-1<=100000 and visited[x-1]==False:
        q.append(x-1)
        visited[x-1]=True
        time[x-1]=time[x]+1
print(time[K])