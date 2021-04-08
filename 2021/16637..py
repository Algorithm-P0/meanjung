import sys
N = int(sys.stdin.readline())
exp = sys.stdin.readline().strip()
nums = []
op = []
ans = -sys.maxsize

def dfs(idx, sub_total):
    global ans
    if idx==len(op):
        ans = max(ans, int(sub_total))
        return
    
    first = str(eval(sub_total + op[idx] + nums[idx+1]))
    dfs(idx+1, first)

    if idx+1<len(op):
        second = str(eval(nums[idx+1] + op[idx+1] + nums[idx+2]))
        second = str(eval(sub_total + op[idx] + second))
        dfs(idx+2, second)

for e in exp:
    if e=='+' or e=='-' or e=='*':
        op.append(e)
    else:
        nums.append(e)

dfs(0, nums[0])
print(ans)
