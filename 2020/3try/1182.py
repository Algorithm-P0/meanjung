import sys
N, S = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
ans = 0
def solve(idx, tmp):
    global S, ans
    if sum(tmp)==S:
        ans+=1
    for i in range(idx+1, N):
        tmp.append(lst[i])
        solve(i, tmp)
        tmp.pop()
for i in range(N):
    solve(i, [lst[i]])
print(ans)
