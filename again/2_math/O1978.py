import sys
N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
count=0
def func(i):
    if i==1:
        return False
    for j in range(2, i):
        if i%j==0:
            return False
    return True
for i in nums:
    if func(i)==True:
        count+=1
print(count)