import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
p, s, m, d = map(int, sys.stdin.readline().split())
res=[]
def cal(lst):
    s = A[0]
    for i in range(N-1):
        if lst[i]=='+':
            s+=A[i+1]
        if lst[i]=='-':
            s-=A[i+1]
        if lst[i]=='*':
            s*=A[i+1]
        if lst[i]=='/':
            s = int(s/A[i+1])
    res.append(s)
def solve(p, s, m, d, lst):
    if len(lst)==N-1:
        cal(lst)
        return
    if p>0:
        lst.append('+')
        solve(p-1, s, m, d, lst)
        lst.pop()
    if s>0:
        lst.append('-')
        solve(p, s-1, m, d, lst)
        lst.pop()
    if m>0:
        lst.append('*')
        solve(p, s, m-1, d, lst)
        lst.pop()
    if d>0:
        lst.append('/')
        solve(p, s, m, d-1, lst)
        lst.pop()

for i in range(4):
    if p>0:
        solve(p-1, s, m, d, ['+'])
    if s>0:
        solve(p, s-1, m, d, ['-'])
    if m>0:
        solve(p, s, m-1, d, ['*'])
    if d>0:
        solve(p, s, m, d-1, ['/'])
print(max(res))
print(min(res))