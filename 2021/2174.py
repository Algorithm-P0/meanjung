# 가로A 세로B 로봇N개
import sys
A, B = map(int, sys.stdin.readline().split())
N, M = map(int, sys.stdin.readline().split())
robotDict = {}
for i in range(N):
    l = sys.stdin.readline().strip().split(maxsplit=2)
    x, y, d = int(l[0]), int(l[1]), l[2]
    robotDict[i+1] = [y, x, d]
# order
# 1 : 왼쪽으로 90도 회전
# 2 : 오른쪽으로 90도 회전
# 3 : 앞으로 한 칸 움직인다

direction = ['N','E','S','W']
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
def check(pIdx, py, px):
    for k in robotDict.keys():
        if pIdx!=k:
            ky, kx, kd = robotDict[k]
            if ky==py and kx==px:
                return k#충돌하는 로봇 인덱스
    return -1# 충돌하지 않음

def simulation(robot, order, repeat):
    y, x, d = robotDict[robot]
    dIdx = direction.index(d)
    # robot의 현재위치, 현재방향
    if order=='F':
        for i in range(1,repeat+1):
            c = check(robot, y+i*dy[dIdx],x+i*dx[dIdx])
            if y+i*dy[dIdx]<=0 or y+i*dy[dIdx]>B or x+i*dx[dIdx]<=0 or x+i*dx[dIdx]>A:
                return 'Robot '+str(robot)+' crashes into the wall'
            elif c!=-1:#충돌한다면
                return 'Robot '+str(robot)+' crashes into robot '+str(c)
            if i==repeat:
                robotDict[robot]=[y+i*dy[dIdx],x+i*dx[dIdx],d]
    elif order=='R':
        dIdx2 = (dIdx+repeat)%4
        robotDict[robot] = [y, x, direction[dIdx2]]
    elif order=='L':
        dIdx2 = (dIdx-repeat)%4
        robotDict[robot] = [y, x, direction[dIdx2]]
    return 'OK'
orderList = []

for _ in range(M):
    l = sys.stdin.readline().strip().split(maxsplit=2)
    robot, order, repeat = int(l[0]), l[1], int(l[2])
    orderList.append([robot, order, repeat])

for robot, order, repeat in orderList:
    result = simulation(robot, order, repeat)
    if result!='OK':
        print(result)
        sys.exit()
print(result)
