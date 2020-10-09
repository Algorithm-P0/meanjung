# 재귀
# 못 품.
import sys
f = str(sys.stdin.readline().strip())
L = int(sys.stdin.readline())
R = int(sys.stdin.readline())
N = int(sys.stdin.readline()) # 초
# 1 -> 132
# 2 -> 211
# 3 -> 232
one, two, three = 0, 0, 0
for i in f:
    if i=="1":
        one+=1
    elif i=="2":
        two+=1
    elif i=="3":
        three+=1

def solve(count, one, two, three):
    if count==N:
        print(one, two, three)
        return
    none = one + 2*two
    ntwo = one + two + 2*three
    nthree = one + three
    solve(count+1, none, ntwo, nthree)

solve(0, one, two, three) # L, R 따지지 않고 마지막의 1, 2, 3의 개수

"""
# 시간초과 풀이
for _ in range(N):
    s=""
    for i in f:
        if i == "1":
            s+="132"
        elif i=="2":
            s+="211"
        elif i=="3":
            s+="232"
    f = s
f = f[L:R+1]
one, two, three = 0, 0, 0
for i in f:
    if i=="1":
        one+=1
    elif i=="2":
        two+=1
    elif i=="3":
        three+=1
print(one, two, three)
"""