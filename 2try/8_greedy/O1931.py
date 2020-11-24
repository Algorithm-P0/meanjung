import sys
N = int(sys.stdin.readline())
conf = []
for _ in range(N):
    s, e = map(int, sys.stdin.readline().split())
    conf.append([s, e])
conf = sorted(conf, key= lambda x: (x[1], x[0]))

end_time = conf[0][1]
count = 1
# 이미 빨리 끝나는 순서대로 정렬되어 있다.
for i in range(1, N):
    if end_time<=conf[i][0]:
        count+=1
        end_time = conf[i][1]
print(count)