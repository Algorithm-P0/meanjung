import sys
from itertools import combinations
N, M = map(int, sys.stdin.readline().split())
graph = []
chicken = []
home = []
for y in range(N):
    g = list(map(int, sys.stdin.readline().split()))
    graph.append(g)
    for x in range(N):
        if graph[y][x]==2:
            chicken.append([y, x])
        elif graph[y][x]==1:
            home.append([y, x])
minv = sys.maxsize
for ch in combinations(chicken, M):
    sumv = 0
    for home_element in home:
        sumv += min([abs(home_element[0]-i[0])+abs(home_element[1]-i[1]) for i in ch])
        if minv <= sumv:
            break
    if sumv < minv:
        minv = sumv
print(minv)