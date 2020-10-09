import sys
N=int(sys.stdin.readline())
tree={}
for _ in range(N):
    r, L, R = list(sys.stdin.readline().split())
    tree[r]=[L, R]

def PreOrder(start):
    if(start == '.'):
        return
    print(start, end="")
    PreOrder(tree[start][0])
    PreOrder(tree[start][1])

def InOrder(start):
    if(start == '.'):
        return
    InOrder(tree[start][0])
    print(start, end="")
    InOrder(tree[start][1])

def PostOrder(start):
    if(start == '.'):
        return
    PostOrder(tree[start][0])
    PostOrder(tree[start][1])
    print(start, end="")

PreOrder('A')
print()
InOrder('A')
print()
PostOrder('A')