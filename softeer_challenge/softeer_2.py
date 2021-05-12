import sys
P, N = map(int, sys.stdin.readline().split())
A = [0]
A.extend(list(map(int, sys.stdin.readline().split())))

ans = 0
P = P % 1000000007
for i in range(1, N+1):
    A[i] = A[i] % 1000000007
    sq = 1
    for j in range(N-i):
        sq = (sq*P) % 1000000007
    ans += (A[i]*(sq % 1000000007))%1000000007
print(ans%1000000007)
# 푸는 방법은 알겠는데 오버플로우 문제같은데 해결을 못하겠음
