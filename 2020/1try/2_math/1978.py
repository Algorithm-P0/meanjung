def checkPrime(num):
    if num == 1 :
        return False
    for i in range(2, num):
        if num%i ==0:
            return False # 합성수
    return True # 소수
import sys

N = int(sys.stdin.readline())
numArr = list(map(int,sys.stdin.readline().split()))
cnt=0
for i in numArr:
    if checkPrime(i) == True:
        cnt+=1
print(cnt)