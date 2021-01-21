import sys
K = int(sys.stdin.readline())
AB=[[1,0]]
for i in range(1, K+1):
    AB.append([AB[i-1][1], AB[i-1][0]+AB[i-1][1]])
print(AB[K][0], AB[K][1])