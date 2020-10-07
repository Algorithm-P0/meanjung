import sys
n = int(sys.stdin.readline())
# 중순위, 후순위가 주어짐
inorder = list(map(int, sys.stdin.readline().split()))
postorder = list(map(int, sys.stdin.readline().split()))
# 전순위를 구하라