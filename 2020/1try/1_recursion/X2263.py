import sys

n = int(sys.stdin.readline())
InOrder = list(map(int, sys.stdin.readline().split()))
PostOrder = list(map(int, sys.stdin.readline().split()))

root = PostOrder[-1]
tree = {}

def solve(root, PostOrder):
    InRootIdx = InOrder.index(root)
    lroot = PostOrder[InRootIdx-1]
    rroot = PostOrder[-1]
    tree[root]=[lroot, root]
    if InRootIdx
    solve(lroot, PostOrder[:InRootIdx])
    solve(rroot, PostOrder[InRootIdx+1:])

solve(root, PostOrder)
print(tree)
