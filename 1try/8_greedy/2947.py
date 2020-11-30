import sys
order = list(map(int, sys.stdin.readline().split()))
for i in range(1, 5):
    for j in range(5-i):
        if order[j]>order[j+1]:
            order[j], order[j+1] = order[j+1], order[j]
            print(*order)