import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
op = list(map(int, sys.stdin.readline().split()))
mmin = 1000000000
mmax = -1000000000

def solve(index, res, add, sub, mul, mod):
    global mmin
    global mmax
    if index>=N:
        mmin = min(mmin, res)
        mmax = max(mmax, res)
        return
    if add:
        solve(index+1, res+A[index], add - 1, sub, mul, mod)
    if sub:
        solve(index+1, res-A[index], add, sub-1, mul, mod)
    if mul:
        solve(index+1, res*A[index], add, sub, mul-1, mod)
    if mod:
        solve(index+1, int(res/A[index]), add, sub, mul, mod-1)

solve(1, A[0], op[0], op[1], op[2], op[3])
print(mmax)
print(mmin)