import sys

height = [int(sys.stdin.readline()) for _ in range(9)]

ans = sum(height)

flag = 0
for i in range(9):
    for j in range(i+1, 9):
        if ans - (height[i]+height[j]) == 100:
            flag = 1
            a = height[i]
            b = height[j]
            height.remove(a)
            height.remove(b)
            break
    if flag == 1:
        break
height.sort()
for i in height:
    print(i)