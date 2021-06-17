import sys
N = int(sys.stdin.readline())
lecture = []
for _ in range(N):
    s, e = map(int, sys.stdin.readline().split())
    lecture.append([e, s])
lecture.sort()
dp = [0]*1000000001
for i in range(N):
    dp[lecture[i][0]]=1
    dp[lecture[i][0]] = max(dp[lecture[i][0]], max(dp[:lecture[i][1]+1])+1)
    print(dp)