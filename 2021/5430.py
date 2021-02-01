# R뒤집기 D버리기
# 꼭 회전/삭제를 직접 하지 않더라도
# l, r 변수로 index를 줄여/늘여가며 해결할 수 있다.
# d는 방향을 나타냄
import sys
T = int(sys.stdin.readline())
for _ in range(T):
    pFunc = sys.stdin.readline().strip()
    n = int(sys.stdin.readline())
    arr = sys.stdin.readline().strip()
    arr = list(arr[1:-1].split(','))
    pFunc.replace('RR', '')
    l, r, d = 0, 0, True
    for p in pFunc:
        if p=='R':
            d = not d
        elif p=='D':
            if d==True:
                l+=1
            else:
                r+=1
    if l+r<=n:
        res = arr[l:n-r]
        if d==True:
            print('['+','.join(res)+']')
        else:
            print('['+','.join(res[::-1])+']')
    else:
        print('error')