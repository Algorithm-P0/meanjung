# 이전순열
import sys
N = int(sys.stdin.readline())
perm = list(map(int, sys.stdin.readline().split()))
if N==1:
    print(-1)
for i in range(N-2,-1,-1):
    if perm[i]>perm[i+1]:
        m = []
        for j in range(i+1, N):# i보다 뒤에 있는 수들 중 perm[i]보다 작은 수 중 가장 큰 수
            if perm[i]>perm[j]:
                m.append(perm[j])
        new_idx = perm.index(max(m))
        perm[i], perm[new_idx] = perm[new_idx], perm[i]
        sorted_part = sorted(perm[i+1:], reverse=True)
        perm[i+1:]=sorted_part
        print(' '.join(map(str, perm)))
        break
    if i==0:
        print(-1)
