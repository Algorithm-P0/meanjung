# i를 n진수로 바꾸는 함수
def convert(i, n):
    T = "0123456789ABCDEF"
    q, r = divmod(i, n)
    if q == 0:
        return T[r]
    else:
        return convert(q, n) + T[r]
def solution(n, t, m, p):
    i = 0
    result = []
    while True:
        converted = convert(i, n)
        result.extend(list(converted))
        if len(result)>=t*m:
            break
        i+=1
    ans = ''
    for i in range(t):
        ans += result[p-1+m*i]
    return ans

solution(2, 4, 2, 1)