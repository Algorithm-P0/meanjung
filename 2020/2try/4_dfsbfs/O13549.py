import sys
from collections import deque
N, K = map(int, sys.stdin.readline().split())
count = [-1]*100001
def bfs(N, K):
    count[N]=0
    q = deque()
    q.append(N)
    while q:
        x = q.popleft()
        if x==K:
            return count[K]
        for i in (2*x, x+1, x-1):
            if 0<=i<=100000:
                if count[i]==-1:
                    if i==2*x:
                        q.appendleft(i)
                        count[i]=count[x]
                    else:
                        q.append(i)
                        count[i]=count[x]+1
print(bfs(N,K))