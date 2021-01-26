import sys
C = int(sys.stdin.readline())
crane = list(map(int, sys.stdin.readline().split()))
crane.sort()
B = int(sys.stdin.readline())
box = list(map(int, sys.stdin.readline().split()))
box.sort()
if box[-1]>crane[-1]:
    ans = -1
else:
    ans = 0
    while len(box)>0:
        for i in range(C):
            for j in range(len(box)-1,-1,-1):
                if box[j]<=crane[i]:
                    del box[j]
                    break
        ans+=1
print(ans)