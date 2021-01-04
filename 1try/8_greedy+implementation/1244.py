# 문제가 이상한듯^^
# 다시 풀어볼 필요 없음
import sys
N = int(sys.stdin.readline())
switch = [0]
switch.extend(list(map(int, sys.stdin.readline().split())))
S = int(sys.stdin.readline())
for _ in range(S):
    sex, num = map(int, sys.stdin.readline().split())
    if sex==1:#남자
        while num<=N:
            if switch[num]==1:
                switch[num]=0
            else:
                switch[num]=1
            num +=num
    else:#여자
        if switch[num]==1:
            switch[num]=0
        else:
            switch[num]=1
        i = 1
        while num-i>=1 and num+i<=N and switch[num-i]==switch[num+1]:
            if switch[num-i]==1:
                switch[num-i]=0
                switch[num+i]=0
            else:
                switch[num-i]=1
                switch[num+i]=1
            i+=1

for i, e in enumerate(switch[1:]):
    if i and not (i%20):
        print()
    print(e, end=" ")