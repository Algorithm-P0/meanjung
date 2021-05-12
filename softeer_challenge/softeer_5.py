import sys
# N사람수 M친분수
N, M = map(int, sys.stdin.readline().split())
# W사람마다 들 수 있는 무게
W = list(map(int, sys.stdin.readline().split()))
# F친분그래프
F = [[] for _ in range(N)]
for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    F[i-1].append(j-1)
    F[j-1].append(i-1)
def solve(i):# 사람index
    for j in F[i]:
        if W[i]<=W[j]:
            return False
    return True
ans = 0
for i in range(N):
    flag = solve(i)
    if flag==True:
        ans += 1
print(ans)