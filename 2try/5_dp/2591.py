# 조금만 더 생각해보자...
import sys
card = sys.stdin.readline().strip()
count = 0
def solve(idx):
    global count
    if idx>=len(card)-1:
        count+=1
        return
    if card[idx+1]!='0':
        solve(idx+1)
    if 1<=int(card[idx:idx+2])<=34:
        solve(idx+2)
solve(0)
print(count)
