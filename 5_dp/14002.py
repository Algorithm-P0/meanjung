# LIS의 길이 + 배열 자체도 구하라...
# 시간복잡도 = O(N^2)
# 어렵다... 중요하다...
import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
dp=[1]*N

for i in range(N):
    for j in range(i):
        if A[j]<A[i]:
            dp[i]=max(dp[i], dp[j]+1)

l_cnt = max(dp)
print(l_cnt)

idx = dp.index(l_cnt)
ans=[]

while idx>=0:
    if dp[idx]==l_cnt:
        ans.append(A[idx])
        l_cnt-=1
    idx-=1
ans.sort(reverse=False)
for a in ans:
    print(a, end=' ')