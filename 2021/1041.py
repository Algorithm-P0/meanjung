import sys
N = int(sys.stdin.readline())
dice = list(map(int, sys.stdin.readline().split()))
if N==1:
    print(sum(dice)-max(dice))
else:
    min1 = min(dice[0], dice[5])
    min2 = min(dice[1], dice[4])
    min3 = min(dice[2], dice[3])
    ans = 0
    ans += 4*(min1+min2+min3)# 3면
    ans += (8*N-12)*(min1+min2+min3-max(min1, min2, min3))# 2면
    ans += (N-2)*(5*N-6)*min(min1, min2, min3)
    print(ans)