import sys
N, K = map(int, sys.stdin.readline().split())
A=[]
for _ in range(N):
    A.append(int(sys.stdin.readline()))
A.sort(reverse=True)
cnt = 0
for a in A:
    if a<=K:
        cnt+=K//a
        K = K % a
print(cnt)