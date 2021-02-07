import sys
N = int(sys.stdin.readline())
RGB = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
firstRed = [[0]*3 for _ in range(N)]
MAX = 10000001
firstRed[0]=[RGB[0][0],MAX,MAX]
for i in range(1, N):
    firstRed[i][0] = RGB[i][0]+min(firstRed[i-1][1], firstRed[i-1][2])
    firstRed[i][1] = RGB[i][1]+min(firstRed[i-1][0], firstRed[i-1][2])
    firstRed[i][2] = RGB[i][2]+min(firstRed[i-1][0], firstRed[i-1][1])

firstGreen = [[0]*3 for _ in range(N)]
firstGreen[0] = [MAX, RGB[0][1], MAX]
for i in range(1, N):
    firstGreen[i][0] = RGB[i][0]+min(firstGreen[i-1][1], firstGreen[i-1][2])
    firstGreen[i][1] = RGB[i][1]+min(firstGreen[i-1][0], firstGreen[i-1][2])
    firstGreen[i][2] = RGB[i][2]+min(firstGreen[i-1][0], firstGreen[i-1][1])

firstBlue = [[0]*3 for _ in range(N)]
firstBlue[0] = [MAX, MAX, RGB[0][2]]
for i in range(1, N):
    firstBlue[i][0] = RGB[i][0]+min(firstBlue[i-1][1], firstBlue[i-1][2])
    firstBlue[i][1] = RGB[i][1]+min(firstBlue[i-1][0], firstBlue[i-1][2])
    firstBlue[i][2] = RGB[i][2]+min(firstBlue[i-1][0], firstBlue[i-1][1])


print(min(firstRed[-1][1], firstRed[-1][2], firstGreen[-1][0], firstGreen[-1][2], firstBlue[-1][0], firstBlue[-1][1]))