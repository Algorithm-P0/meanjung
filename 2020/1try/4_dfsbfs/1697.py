# 수빈 : N, 동생 : K
import sys
N, K =map(int, sys.stdin.readline().split())
visited=[False]*100001
time=[0]*100001
q=[N]
visited[N]=True
while q:
    x=q.pop(0)
    if x==K:
        break
    if 0<=x+1<=100000 and visited[x+1]==False:
        q.append(x+1)
        visited[x+1]=True
        time[x+1]=time[x]+1
    if 0<=x-1<=100000 and visited[x-1]==False:
        q.append(x-1)
        visited[x-1]=True
        time[x-1]=time[x]+1
    if 0<=2*x<=100000 and visited[2*x]==False:
        q.append(2*x)
        visited[2*x]=True
        time[2*x]=time[x]+1
print(time[K])