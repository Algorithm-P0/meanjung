import sys
from collections import deque
gear = {}
# 재귀
# deque rotate
# 나눠서 생각하기
def check_right(i, d):
    if i>4 or gear[i-1][2]==gear[i][6]:
        return
    if gear[i-1][2]!=gear[i][6]:
        check_right(i+1, -d)
        gear[i].rotate(d)
def check_left(i, d):
    if i<1 or gear[i][2]==gear[i+1][6]:
        return
    if gear[i+1][6]!=gear[i][2]:
        check_left(i-1, -d)
        gear[i].rotate(d)

for i in range(1,5):
    gear[i]=deque(list(map(int, list(sys.stdin.readline().strip()))))
K = int(sys.stdin.readline())
for _ in range(K):
    i, d = map(int, sys.stdin.readline().split())
    check_right(i+1, -d)
    check_left(i-1, -d)
    gear[i].rotate(d)
    # d -1:반시계 1:시계
result = 0
for i in range(4):
    result += (2**i)*gear[i+1][0]
print(result)