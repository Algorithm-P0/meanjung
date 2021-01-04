"""
  A B C D E F G H
8
7
6
5
4
3
2
1
"""
import sys
kingPos, stonePos, N = map(str, sys.stdin.readline().split())
kingPosX = ord(kingPos[0])-ord('A')
kingPosY = 8-int(kingPos[1])
stonePosX = ord(stonePos[0])-ord('A')
stonePosY = 8-int(stonePos[1])
#idx:0, 1, 2, 3, 4,  5,  6,  7
#    R, L, B, T, RT, LT, RB, LB
dy = [0, 0, 1, -1, -1, -1, 1, 1]
dx = [1, -1, 0, 0, 1, -1, 1, -1]
for i in range(int(N)):
    M = sys.stdin.readline().strip()
    if M=='R':
        idx = 0
    elif M=='L':
        idx = 1
    elif M=='B':
        idx = 2
    elif M=='T':
        idx = 3
    elif M=='RT':
        idx = 4
    elif M=='LT':
        idx = 5
    elif M=='RB':
        idx = 6
    elif M=='LB':
        idx = 7
    if kingPosY+dy[idx]==stonePosY and kingPosX+dx[idx]==stonePosX:
        if stonePosY+dy[idx]<0 or stonePosY+dy[idx]>=8 or stonePosX+dx[idx]<0 or stonePosX+dx[idx]>=8:
            continue
        if kingPosY+dy[idx]<0 or kingPosY+dy[idx]>=8 or kingPosX+dx[idx]<0 or kingPosX+dx[idx]>=8:
            continue
        stonePosX, stonePosY = stonePosX+dx[idx], stonePosY+dy[idx]
        kingPosX, kingPosY = kingPosX+dx[idx], kingPosY+dy[idx]
    else:
        if kingPosY+dy[idx]<0 or kingPosY+dy[idx]>=8 or kingPosX+dx[idx]<0 or kingPosX+dx[idx]>=8:
            continue
        kingPosX, kingPosY = kingPosX+dx[idx], kingPosY+dy[idx]

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
print(alphabet[kingPosX]+str(8-kingPosY))
print(alphabet[stonePosX]+str(8-stonePosY))