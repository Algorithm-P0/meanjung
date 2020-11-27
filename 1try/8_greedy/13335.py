import sys
from collections import deque
n, w, L = map(int, sys.stdin.readline().split())
truck = deque(list(map(int, sys.stdin.readline().split())))
q = deque()
t = deque()
q.append(truck.popleft())
t.append(1)
time = 1
while q:
    time+=1
    if time-t[0]==w:
        q.popleft()
        t.popleft()
    if truck:
        if sum(q)+truck[0]<=L:
            q.append(truck.popleft())
            t.append(time)
print(time)