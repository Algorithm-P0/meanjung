import sys
n = int(sys.stdin.readline())
graph = [[0]*101 for _ in range(101)]
s = 0
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            if graph[j][i]==0:
                graph[j][i]=1
                s+=1
            else:
                continue
print(s)