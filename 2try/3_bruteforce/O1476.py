import sys
E, S, M = map(int, sys.stdin.readline().split())
if E == 15:
    E = 0
if S == 28:
    S = 0
if M == 19:
    M = 0
year = 1
while True:
    if year%15==E and year%28==S and year%19==M:
        break
    year+=1
print(year)