import sys
# 재귀 허용 깊이를 수동으로 늘려주는.
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())
# 중순위, 후순위가 주어짐
inorder = list(map(int, sys.stdin.readline().split()))
postorder = list(map(int, sys.stdin.readline().split()))

position = {}
# position[i] : inorder[i]의 index
for i in range(n):
    position[inorder[i]]=i
def solve(in_start, in_end, post_start, post_end):
    if in_start>in_end or post_start>post_end:
        return
    root = postorder[post_end]
    print(root, end = ' ')
    p = position[root] # root의 inorder에서의 index
    left = p - in_start 
    solve(in_start, p-1, post_start, post_start+left-1)
    solve(p+1, in_end, post_start+left, post_end-1)
solve(0, n-1, 0, n-1)