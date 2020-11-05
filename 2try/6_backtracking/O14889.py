import sys
from copy import deepcopy

N = int(sys.stdin.readline())
cap= []
for _ in range(N):
    cap.append(list(map(int, sys.stdin.readline().split())))
res = sys.maxsize
temp = [0]
def dif(temp1):
    global res
    temp2 = []
    for i in range(N):
        if i in temp1:
            continue
        temp2.append(i)
    temp1_n = 0
    temp2_n = 0
    for i in range(N//2-1):
        for j in range(i+1, N//2):
            a,b = temp1[i], temp1[j]
            c,d = temp2[i], temp2[j]
            temp1_n+=cap[a][b]+cap[b][a]
            temp2_n+=cap[c][d]+cap[d][c]
    res = min(res, abs(temp1_n-temp2_n))
def dfs(temp):
    t = deepcopy(temp)
    if len(t)==N//2:
        dif(t)
        return
    for i in range(t[-1]+1, N):
        t.append(i)
        dfs(t)
        t.pop()
dfs(temp)
print(res)