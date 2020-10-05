# 트리, 재귀
import sys
N = int(sys.stdin.readline())

# dictionary(key: value)를 이용해 해결
# dictionary : {'key':'value', ...} 형식
# value에 배열 들어갈 수 있음
# key에 정수 가능(' 없이)

tree={}
for _ in range(N):
    root, left, right = sys.stdin.readline().strip().split()
    tree[root]=[left, right]
def preOrder(start): # start가 index가 아니라 실제 char 값
    if start=='.':
        return
    print(start, end='')
    preOrder(tree[start][0])
    preOrder(tree[start][1])
preOrder('A')
print()
def inOrder(start):
    if start=='.':
        return
    inOrder(tree[start][0])
    print(start, end='')
    inOrder(tree[start][1])
inOrder('A')
print()
def postOrder(start):
    if start=='.':
        return
    postOrder(tree[start][0])
    postOrder(tree[start][1])
    print(start, end='')
postOrder('A')
print()

"""
# 메모리초과 코드
tree=['.']*(2**26)
tree[0]='A'
for _ in range(N):
    root, left, right = sys.stdin.readline().strip().split()
    rootIdx = tree.index(root)
    tree[2*rootIdx+1]=left
    tree[2*rootIdx+2]=right
def preOrder(idx):# 전위순회 -> Root Left Right
    if tree[idx]=='.':
        return
    print(tree[idx], end='')
    preOrder(2*idx+1)
    preOrder(2*idx+2)
preOrder(0)
print()
def inOrder(idx): # 중위순회 -> Left Root Right
    if tree[idx]=='.':
        return
    inOrder(2*idx+1)
    print(tree[idx], end="")
    inOrder(2*idx+2)
inOrder(0)
print()
def postOrder(idx):# 후위순회 -> Left Right Root
    if tree[idx]=='.':
        return
    postOrder(2*idx+1)
    postOrder(2*idx+2)
    print(tree[idx], end="")
postOrder(0)
"""