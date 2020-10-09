import sys
import itertools

def solve(arr):
    s = list(itertools.combinations(arr[1:], 6))
    for com in s:
        for k in com:
            print(k, end =" ")
        print()

while True:
    S = list(map(int, sys.stdin.readline().split()))
    if S==[0]:
        break
    solve(S)
    print()