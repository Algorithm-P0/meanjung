import sys
from collections import deque
def check_right(start, dirs):
    if start>4 or gear[start-1][2]==gear[start][6]:
        return
    if gear[start-1][2]!=gear[start][6]:
        check_right(start+1, -dirs)
        gear[start].rotate(dirs)
        # 음수: 왼쪽으로 회전/ 양수: 오른쪽으로 회전
def check_left(start, dirs):
    if start<1 or gear[start][2]==gear[start+1][6]:
        return
    if gear[start+1][6]!=gear[start][2]:
        check_left(start-1, -dirs)
        gear[start].rotate(dirs)

gear = {}
for i in range(1, 5):
    gear[i] = deque(list(map(int, list(sys.stdin.readline().strip()))))
N = int(sys.stdin.readline())
for _ in range(N):
    n, d = map(int, sys.stdin.readline().split())
    check_right(n+1, -d)
    check_left(n-1, -d)
    gear[n].rotate(d)
result = 0
for i in range(4):
    result+=(2**i)*gear[i+1][0]
print(result)