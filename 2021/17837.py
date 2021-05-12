import sys
N, K = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
horse = {}
for k in range(1, K+1):
    y, x, d = map(int, sys.stdin.readline().split())
    horse[k]=[y-1, x-1, d]


