import sys
def init(dir, dis, N, M):
    if dir==1:
        y = 0
        x = dis
    elif dir==2:
        y = M
        x = dis
    elif dir==3:
        y = dis
        x = 0
    else:
        y = dis
        x = N
    return dir, y, x
N, M = map(int, sys.stdin.readline().split())
# N가로 M세로
K = int(sys.stdin.readline())
kList = []
for _ in range(K):
    dir, dis = map(int, sys.stdin.readline().split())
    dir, y, x = init(dir, dis, N, M)
    kList.append([dir, y, x])
my_dir, my_dis = map(int, sys.stdin.readline().split())
my_dir, my_y, my_x = init(my_dir, my_dis, N, M)

temp = 0
ans = 0

if my_dir==1:
    temp = 2
elif my_dir==2:
    temp = 1
elif my_dir==3:
    temp = 4
else:
    temp = 3

for dir, y, x in kList:
    if dir==temp:
        if dir==1 or dir==2:
            ans += min(my_y+y+my_x+x, my_y+y+N-my_x+N-x)
        else:
            ans += min(M-my_y+M-y+my_x+x, my_y+y+my_x+x)
    else:
        ans += abs(my_y-y)+abs(my_x-x)
print(ans)
