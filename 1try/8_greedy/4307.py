import sys
T = int(sys.stdin.readline())
def minTime(l, n, ant):
    ans = 0
    for i in range(n):
        if ant[i]>l//2:
            ans = max(ans, l-ant[i])
        else:
            ans = max(ans, ant[i])
    return ans
# 만나면 반대방향으로 진행한다는 것은 무시해도 된다.
# 교차하는 것이라 생각하면 된다.
def maxTime(l, n, ant):
    ans = 0
    for i in range(n):
        if ant[i]>l//2:
            ans = max(ans, ant[i])
        else:
            ans = max(ans, l-ant[i])
    return ans
for _ in range(T):
    l, n = map(int, sys.stdin.readline().split())
    ant = []
    for _ in range(n):
        ant.append(int(sys.stdin.readline()))
    ant.sort()
    print(minTime(l, n, ant), end=" ")
    print(maxTime(l, n, ant))
