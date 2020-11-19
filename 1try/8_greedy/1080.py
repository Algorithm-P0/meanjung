import sys
N, M = map(int, sys.stdin.readline().split())
A = []
B = []
res = 0
for _ in range(N):
    A.append(list(map(str, sys.stdin.readline().strip())))
for _ in range(N):
    B.append(list(map(str, sys.stdin.readline().strip())))
def check():
    for y in range(N):
        for x in range(M):
            if A[y][x]!=B[y][x]:
                return False
    return True
def change(y, x):
    for i in range(y, y+3):
        for j in range(x, x+3):
            if A[i][j]=='0':
                A[i][j]='1'
            elif A[i][j]=='1':
                A[i][j]='0'
for y in range(N-3+1):
    for x in range(M-3+1):
        if A[y][x]!=B[y][x]:
            res+=1
            change(y, x)
if check()==True:
    print(res)
else:
    print(-1)