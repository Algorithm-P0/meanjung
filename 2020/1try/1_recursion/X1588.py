import sys

first = str(sys.stdin.readline().strip())
Left = int(sys.stdin.readline())
Right = int(sys.stdin.readline())
N = int(sys.stdin.readline())

def switch(numList):
    strr = ""
    for i in numList:
        if i == "1":
            strr += "132"
        elif i == "2":
            strr += "211"
        else:
            strr += "232"
    return strr
import sys

count = [0,0,0]

for i in range(N):
    first = switch(first)

print(first)

for i in range(Left, Right+1):
    count[int(first[i])-1]+=1

for i in count:
    print(i, end=" ")

# 시간초과
