import sys
N = int(sys.stdin.readline())
student = []
for _ in range(N):
    student.append(int(sys.stdin.readline()))
dp = [0]*N
dp[0]=1
for i in range(1, N):
    temp = []
    for j in range(i):
        if student[i]>student[j]:
            temp.append(dp[j])
    if not temp:
        dp[i]=1
    else:
        dp[i]=max(temp)+1
print(N-max(dp))
"""
가장 긴 증가하는 부분 수열의 길이를 구해서
N에서 빼면 된다.
즉, 가장 긴 증가하는 부분 수열 외의 값들을 옮기면 된다.
dp[i] = i까지 가장 긴 증가하는 부분수열
"""