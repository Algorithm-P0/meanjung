import sys
N = int(sys.stdin.readline())
def solve(lst):
    if len(lst)==N:
        print(' '.join(map(str, lst)))
        return
    for i in range(1, N+1):
        if i not in lst:
            lst.append(i)
            solve(lst)
            lst.pop()
for i in range(1, N+1):
    solve([i])