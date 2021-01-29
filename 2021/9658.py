import sys
N = int(sys.stdin.readline())
# 0: 창영 승/ 1: 상근 승
res = [0,0,1,0,1]
for i in range(5, N+1):
    if res[i-1]==1 and res[i-3]==1 and res[i-4]==1:
        res.append(0) # 창영 승
    else:
        res.append(1) # 상근 승
if res[N]==0:
    print('CY')
else:
    print('SK')