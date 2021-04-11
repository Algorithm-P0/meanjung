"""
# 시간초과 풀이
import sys
N, M, K = map(int, sys.stdin.readline().split())
# 크기N/ 초기나무개수M/ K년이 지난후 살아남은 나무의 수
food = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# 추가로 뿌릴 양분
tree = []# 해당 위치의 나무나이
for _ in range(M):
    y, x, z = map(int, sys.stdin.readline().split())
    tree.append([z, y-1, x-1])#나이, y좌표, x좌표

graph = [[5]*N for _ in range(N)] #양분
dy = [-1,1,0,0,1,1,-1,-1]
dx = [0,0,-1,1,-1,1,1,-1]
year = 0
while year!=K:
    tree.sort()
    alive_tree = []#tree중 봄에 살아남은 나무
    die = []#tree중 봄에 죽은 나무
    # spring
    for z, y, x in tree:
        if graph[y][x]>=z:#나이만큼 양분을 먹을 수 있다면
            alive_tree.append([z+1, y, x])
            graph[y][x]-=z
        else:
            die.append([z, y, x])
    # summer
    for z, y, x in die:
        graph[y][x]+=z//2
    # august
    for z, y, x in alive_tree:
        if z%5==0:
            for i in range(8):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0<=ny<N and 0<=nx<N:
                    alive_tree.append([1, ny, nx])
    # winter
    for y in range(N):
        for x in range(N):
            graph[y][x]+=food[y][x]
    tree = alive_tree
    year+=1
print(len(tree))
"""
import sys
from collections import deque


def spring_summer():
    for y in range(N):
        for x in range(N):
            tree_len = len(tree[y][x])
            for k in range(tree_len):
                if tree[y][x][k]<=graph[y][x]:
                    graph[y][x]-=tree[y][x][k]
                    tree[y][x][k]+=1
                else:
                    for _ in range(k, tree_len):
                        graph[y][x]+=tree[y][x].pop()//2
                    break

def fall_winter():
    for y in range(N):
        for x in range(N):
            for k in tree[y][x]:
                if k%5==0:
                    for i in range(8):
                        ny = y + dy[i]
                        nx = x + dx[i]
                        if 0<=ny<N and 0<=nx<N:
                            tree[ny][nx].appendleft(1)
            graph[y][x]+=food[y][x]

dy = [-1,1,0,0,1,1,-1,-1]
dx = [0,0,-1,1,-1,1,1,-1]
N, M, K = map(int, sys.stdin.readline().split())

graph = [[5]*N for _ in range(N)]
food = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
tree = [[deque() for _ in range(N)] for _ in range(N)]

for _ in range(M):
    y, x, z = map(int, sys.stdin.readline().split())
    tree[y-1][x-1].append(z)

for _ in range(K):
    spring_summer()
    fall_winter()
ans = 0
for y in range(N):
    for x in range(N):
        ans += len(tree[y][x])
print(ans)