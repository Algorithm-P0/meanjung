import sys
def AC(P, n, arr):
    P.replace('RR', '')
    l, r, d = 0, 0, True
    for p in P:
        if p=='R':
            d = not d
        elif p=='D':
            if d==True:
                l+=1
            else:
                r+=1
    if l+r<=n:
        res=arr[l:n-r]
        if d:
            return '['+','.join(res)+']'
        else:
            return '['+','.join(res[::-1])+']'
    else:
        return 'error'
T = int(sys.stdin.readline())
for _ in range(T):
    P = sys.stdin.readline().strip()
    n = int(sys.stdin.readline())
    arr = sys.stdin.readline().strip()[1:-1].split(',')
    print(AC(P, n, arr))