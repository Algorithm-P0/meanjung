import sys
N = int(sys.stdin.readline())
s=[]
def backTracking(idx):
    for i in range(1, idx//2+1):# 나쁜수열
        if s[-i:]==s[-2*i:-i]:
            return -1
    if idx==N:
        for i in range(N):
            print(s[i], end='')
        return 0
    for i in (1,2,3):
        s.append(i)
        if backTracking(idx+1)==0:
            return 0
        s.pop()
backTracking(0)