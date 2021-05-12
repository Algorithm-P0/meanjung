import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

ascArr = [1]*N
for i in range(1, N):
    for j in range(i):
        if A[j] < A[i]:
            ascArr[i] = max(ascArr[i], ascArr[j]+1)

descArr = [1]*N
for i in range(N-2, -1, -1):
    for j in range(i+1, N):
        if A[j] < A[i]:
            descArr[i] = max(descArr[i], descArr[j]+1)

sumArr = [ascArr[i]+descArr[i]-1 for i in range(N)]
print(max(sumArr))
# 문제가 이상함 -.-
# 백준 가장 긴 바이토닉 부분 수열과 동일한 문제인 것으로 판단되는데 그 풀이가 틀리는 게 이상..