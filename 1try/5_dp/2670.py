import sys
N=int(sys.stdin.readline())
nums=[]
for _ in range(N):
    nums.append(float(sys.stdin.readline()))
dp=[0]*N
dp[0]=nums[0]
for i in range(N):
    dp[i]=max(nums[i], dp[i-1]*nums[i])
print('%.3f'%max(dp))