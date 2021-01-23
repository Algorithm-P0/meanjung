import sys
N, L = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
cnt = 0
def check(lst):
    sw = [False]*N
    for i in range(N-1):
        if lst[i]==lst[i+1]:
            continue
        if abs(lst[i]-lst[i+1])>1:
            return False
        if lst[i]>lst[i+1]:
            temp = lst[i+1]
            for j in range(i+1, i+L+1):
                if 0<=j<N:
                    if lst[j]!=temp:
                        return False
                    if sw[j]==True:
                        return False
                    sw[j]=True
                else:
                    return False
        else:
            temp = lst[i]
            for j in range(i, i-L, -1):
                if 0<=j<N:
                    if lst[j]!=temp:
                        return False
                    if sw[j]==True:
                        return False
                    sw[j]=True
                else:
                    return False
    return True
for g in graph:
    if check(g):
        cnt+=1
for x in range(N):
    temp = []
    for y in range(N):
        temp.append(graph[y][x])
    if check(temp):
        cnt+=1
print(cnt)