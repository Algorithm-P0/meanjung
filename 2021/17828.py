import sys
N, X = map(int, sys.stdin.readline().split())
if N>X or N*26<X:
    print('!')
else:
    res = ['A']*N
    X -= N
    i = N-1

    while X>0:
        if X>=25:
            res[i] = 'Z'
            i-=1
            X-=25
        else:
            res[i]=chr(X+ord('A'))
            break
    print(''.join(res))