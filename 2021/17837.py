import sys
N, K = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
horse = {}
for k in range(K):
    y, x, d = map(int, sys.stdin.readline().split())
    horse[k]=[y-1, x-1, d]
print(horse)
