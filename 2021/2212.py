import sys
N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
sensor = list(map(int, sys.stdin.readline().split()))
sensor.sort()
dif = []
for i in range(N-1):
    dif.append(sensor[i+1]-sensor[i])
dif.sort()
for _ in range(K-1):
    if len(dif)==0:
        print(0)
        sys.exit()
    dif.pop(-1)
print(sum(dif))
