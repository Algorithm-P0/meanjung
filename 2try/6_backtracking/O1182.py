import sys
N, S = map(int, sys.stdin.readline().split())
nlist = list(map(int, sys.stdin.readline().split()))
cnt=0
def solve(idx, lst):
    global cnt
    if sum(lst)==S:
        cnt+=1
    for i in range(idx+1, N):
        lst.append(nlist[i])
        solve(i, lst)
        lst.pop()
for i in range(N):
    solve(i, [nlist[i]])
print(cnt)