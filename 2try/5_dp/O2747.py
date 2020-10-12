import sys
n = int(sys.stdin.readline())
# 재귀 + 메모이제이션
cache=[-1]*(n+1)
ret = 0
def fibo(n):
    global ret
    if n==0:
        return 0
    if n==1:
        return 1
    if cache[n]!=-1:
        return cache[n]
    else:
        cache[n] = fibo(n-1)+fibo(n-2)
        return cache[n]
print(fibo(n))
"""
# 혹은 반복문
dp=[0]*(46)
dp[1]=1
for i in range(2, n+1):
    dp[i]=dp[i-1]+dp[i-2]
print(dp[n])
"""