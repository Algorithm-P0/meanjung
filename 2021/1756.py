import sys
D, N = map(int, sys.stdin.readline().split())
ovens = list(map(int, sys.stdin.readline().split()))
pizza = list(map(int, sys.stdin.readline().split()))

for i in range(1, D):
    ovens[i] = min(ovens[i], ovens[i-1])

pizzaIdx = 0
depth = D-1
for i in reversed(range(D)):
    if pizzaIdx>=len(pizza):
        print(depth+1)
        sys.exit()
    if ovens[i]>=pizza[pizzaIdx]:
        pizzaIdx+=1
        depth=i
print(0)