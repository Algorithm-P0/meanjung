import sys
from collections import deque
# w다리의 길이 L다리의 최대하중
n, w, L = map(int,sys.stdin.readline().split())
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
"""
# 내가 생각한 로직
# 나갈 트럭들은 나가고
# 다리위의 트럭의 무게합을 구하고
# 들어올 트럭 + 다리위의 트럭의 무게합 <= L
# 이라면 on에 t넣고 on배열 update
# L보다 크다면 on만 update
"""
