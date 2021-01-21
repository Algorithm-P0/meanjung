import sys
N = int(sys.stdin.readline())
nums = []
for _ in range(N):
    nums.append(float(sys.stdin.readline()))
dp=[nums[0]]
for i in range(1, N):
    dp.append(max(dp[i-1]*nums[i], nums[i]))
print('%.3f'%max(dp))