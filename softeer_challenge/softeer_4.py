import sys
W, N = map(int, sys.stdin.readline().split())
lst = []
for _ in range(N):
    m, p = map(int, sys.stdin.readline().split())
    lst.append([p,m])
lst.sort(reverse=True)
res = 0

for i in range(N):
    if W==0:
        break
    if W>=lst[i][1]:
        res += lst[i][0]*lst[i][1]
        W-=lst[i][1]
    else:# W<lst[i][1]
        res += W*lst[i][0]
        W=0
print(res)
