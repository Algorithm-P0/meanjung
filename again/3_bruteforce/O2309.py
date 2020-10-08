import sys
sys.setrecursionlimit(10**6)
people = [int(sys.stdin.readline()) for _ in range(9)]
ssum = sum(people)
def solve(cnt, idx, lst):
    if cnt==2:
        if ssum-sum(lst)==100:
            people.remove(lst[0])
            people.remove(lst[1])
            people.sort()
            for p in people:
                print(p)
            sys.exit()
    for i in range(idx+1, 9):
        lst.append(people[i])
        solve(cnt+1, i, lst)
        lst.pop()

for i in range(8):
    solve(1, i, [people[i]])