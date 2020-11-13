import sys
N = int(sys.stdin.readline())
tree = [[0]*(N+1) for _ in range(N+1)]
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    tree[a][b]=1
    tree[b][a]=1
M = int(sys.stdin.readline())
mList = []
for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    mList.append([x, y])
