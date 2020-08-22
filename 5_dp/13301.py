import sys
N=int(sys.stdin.readline())
tile=[[0,0],[1,4]]
for _ in range(N-1):
    x=tile[-1][0]+tile[-2][0]
    tile.append([x, tile[-1][1]+2*x])
print(tile[N][1])