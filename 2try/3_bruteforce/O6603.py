import sys
def solve(idx, lst, k):
    if len(lst)==6:
        print(' '.join(map(str, lst)))
        return
    for i in range(idx+1, k+1):
        lst.append(klist[i])
        solve(i, lst, k)
        lst.pop()

while True:
    klist = list(map(int, sys.stdin.readline().split()))
    if klist[0]==0:
        break
    for i in range(1, klist[0]-6+2):
        solve(i, [klist[i]], klist[0])
    print()